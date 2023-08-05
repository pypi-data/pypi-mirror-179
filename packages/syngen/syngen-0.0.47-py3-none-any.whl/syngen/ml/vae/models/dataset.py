from typing import Set, Dict, Optional, List
from dataclasses import dataclass

from loguru import logger
import numpy as np
import dill
import pandas as pd
from scipy.stats import gaussian_kde

from syngen.ml.vae.models.features import InverseTransformer
from syngen.ml.vae.models.features import (
    CategoricalFeature,
    CharBasedTextFeature,
    ContinuousFeature,
    DateFeature,
    BinaryFeature,
)
from syngen.ml.pipeline.pipeline import (
    data_pipeline,
    get_nan_labels,
    nan_labels_to_float
)


@dataclass
class Dataset:
    df: pd.DataFrame
    metadata: Optional[Dict]
    table_name: str
    fk_kde_path: str
    features: Dict
    columns: Dict
    is_fitted: bool
    all_columns: List
    null_num_column_names: List
    nan_labels_dict: Dict

    def __set_pk_key(self, config_of_keys: Dict):
        """
        Set up primary key for the table
        """
        self.primary_keys_mapping = {
            key: value for (key, value) in config_of_keys.items()
            if config_of_keys.get(key).get("type") == "PK"
        }
        self.primary_keys_list = list(self.primary_keys_mapping.keys())
        self.primary_key_name = self.primary_keys_list[0] if self.primary_keys_list else None

        if self.primary_key_name:
            logger.info(f"The primary key name was set: {self.primary_key_name}")
        if self.primary_key_name is None:
            logger.info("No primary key was set.")

    def __set_uq_keys(self, config_of_keys: Dict):
        """
        Set up unique keys for the table
        """
        self.unique_keys_mapping = {
            key: value for (key, value) in config_of_keys.items()
            if config_of_keys.get(key).get("type") == "UQ"
        }
        self.unique_keys_mapping_list = list(self.unique_keys_mapping.keys())
        self.unique_keys_list = self.unique_keys_mapping_list if self.unique_keys_mapping_list else []

        if self.unique_keys_list:
            logger.info(f"The unique keys were set: {self.unique_keys_list}")
        if not self.unique_keys_list:
            logger.info("No unique keys were set.")

    def __set_fk_keys(self, config_of_keys: Dict):
        """
        Set up foreign keys for the table
        """
        self.foreign_keys_mapping = {
            key: value for (key, value) in config_of_keys.items()
            if config_of_keys.get(key).get("type") == "FK"
        }
        self.foreign_keys_list = list(self.foreign_keys_mapping.keys())
        fk_columns_lists = [val['columns'] for val in self.foreign_keys_mapping.values()]
        self.fk_columns = [col for fk_cols in fk_columns_lists for col in fk_cols]

        if self.foreign_keys_list:
            logger.info(f"The following foreign keys were set: {self.foreign_keys_list}")
        if not self.foreign_keys_list:
            logger.info("No foreign keys were set.")

    def __set_types(self, pk_uq_keys_mapping, str_columns, categ_columns, date_columns):
        """
        Set up list of data types of primary and unique keys
        """
        self.pk_uq_keys_types = {}
        for key_name, config in pk_uq_keys_mapping.items():
            key_columns = config.get("columns")
            for column in key_columns:
                column_type = str if column in (str_columns | categ_columns | date_columns) else float
                self.pk_uq_keys_types[column] = column_type

    def __set_metadata(self, metadata: dict, table_name: str):
        config_of_keys = metadata.get(table_name, {}).get("keys")

        if config_of_keys is not None:
            self.__set_pk_key(config_of_keys)
            self.__set_uq_keys(config_of_keys)
            self.__set_fk_keys(config_of_keys)
        else:
            self.primary_keys_mapping = {}
            self.unique_keys_mapping = {}
            self.foreign_keys_mapping = {}

    def set_metadata(self):
        self.__set_metadata(self.metadata, self.table_name)

    def assign_feature(self, feature, columns):
        name = feature.name

        if name in self.features:
            raise Exception("%s is already contained in features" % name)

        if not isinstance(columns, (list, tuple)):
            columns = [columns]

        self.features[name] = feature
        self.columns[name] = columns

    def set_nan_params(self, nan_labels: dict):
        """Save params that are used to keep and replicate nan and empty values

        Args:
            nan_labels (dict): dictionary that matches column name to the label of missing value
                               (e.g. {'Score': 'Not available'})
        """
        self.nan_labels_dict = nan_labels

    def fit(self, data):
        for name, feature in self.features.items():
            feature.fit(data[self.columns[name]])

        self.all_columns = [col for col in self.columns]
        self.is_fitted = True

    def transform(self, data, excluded_features=set()):
        transformed_features = list()
        for name, feature in self.features.items():
            if name not in (excluded_features and self.foreign_keys_list):
                transformed_features.append(feature.transform(data[self.columns[name]]))
        return transformed_features

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

    def _check_count_features(self, data):
        return (len(data) == len(self.features)) or (len(data) + len(self.foreign_keys_list) == len(self.features))

    def inverse_transform(self, data, excluded_features=set()):
        inverse_transformed_data = list()
        column_names = list()
        if not isinstance(data, list):
            data = [data]
        assert self._check_count_features(data)

        self.inverse_transformers = {}

        for transformed_data, (name, feature) in zip(data, self.features.items()):
            if name not in excluded_features and name not in self.foreign_keys_list:
                column_names.extend(self.columns[name])
                inverse_transformed_data.append(
                    feature.inverse_transform(transformed_data)
                )
                self.inverse_transformers[name] = InverseTransformer(
                    name, feature.inverse_transform
                )

        stacked_data = np.column_stack(inverse_transformed_data)
        data = pd.DataFrame(stacked_data, columns=column_names)

        return data

    def _preprocess_str_params(self, feature: str):
        self.df[feature] = self.df[feature].fillna("")
        max_len = int(self.df[feature].apply(lambda line: len(line)).max())
        if 1 < max_len < 7:
            rnn_units = 32

        if 6 < max_len < 13:
            rnn_units = 128

        if 12 < max_len < 17:
            rnn_units = 256

        if max_len > 16:
            rnn_units = 512

        return max_len, rnn_units

    def _preprocess_nan_cols(
        self, feature: str, fillna_strategy: str = None
    ) -> tuple:
        """Fill NaN values in numeric column with some value according to strategy.
        Fill NaN values in string columns can only work in 'mode' strategy.
        If NaN values exist additional column is created and added to DataFrame.
        This column has value of 1 in case corresponding row contains NaN and 0 otherwise.
        New column name is built like 'column name'+'_null'.

        Args:
            feature (str): Feature name.
            fillna_strategy (str, optional): Can be 'mean', 'mode' or None.
                                             If None NaN values in column are replaced with 0.
                                             Defaults to None.
                                             Note: string columns only work with 'mode'.

        Returns:
            tuple: Tuple that consists of either feature name or both feature name and new null feature name.
        """
        isnull_feature = pd.isnull(self.df[feature])

        if isnull_feature.any():
            nan_number = isnull_feature.sum()
            logger.info(f"Column {feature} contains {nan_number} ({round(nan_number * 100 / len(isnull_feature))}%) "
                        f"empty values out of {len(isnull_feature)}. Filling them with {fillna_strategy or 'zero'}.")
            if fillna_strategy == "mean":
                fillna_value = self.df[feature].mean()
            elif fillna_strategy == "mode":
                fillna_value = self.df[feature].mode().sample(1).values[0]
            else:
                fillna_value = 0

            feature_null = feature + "_null"
            self.df[feature_null] = isnull_feature.astype(int)
            self.df[feature] = self.df[feature].fillna(fillna_value)
            return (feature, feature_null)
        else:
            return (feature,)

    def _preprocess_categ_params(self, feature: str):
        self.df[feature] = self.df[feature].fillna("?").astype(str)
        return feature

    def _preprocess_fk_params(self):
        for fk in self.foreign_keys_list:
            fk_columns = self.foreign_keys_mapping.get(fk).get("columns")
            for fk_column in fk_columns:
                fk_column = self.df[fk_column]
                if fk_column.dtype != "object":
                    kde = gaussian_kde(fk_column)
                    with open(self.fk_kde_path, "wb") as file:
                        dill.dump(kde, file)
                    logger.info(f"KDE artifacts saved to {self.fk_kde_path}")
            yield fk, fk_columns

    def __drop_fk_columns(self, *args: Set[str]) -> object:
        """
        Drop columns which defined as foreign key
        """
        float_columns, int_columns, str_columns, categ_columns = args
        for fk, fk_columns in self._preprocess_fk_params():
            for fk_column in fk_columns:
                self.df = self.df.drop(fk_column, axis=1)
                float_columns.discard(fk_column)
                int_columns.discard(fk_column)
                str_columns.discard(fk_column)
                categ_columns.discard(fk_column)
                logger.debug(f"The column - {fk_column} of foreign key {fk} dropped from training "
                             f"and will be sampled from the PK table")
        return float_columns, int_columns, str_columns, categ_columns

    def __sample_only_joined_rows(self, fk):
        # for fk in self.foreign_keys_list
        references = self.foreign_keys_mapping.get(fk).get("references")
        pk_table = references.get("table")
        pk_table_data = pd.read_csv(f"model_artifacts/tmp_store/{pk_table}/input_data_{pk_table}.csv",
                                    engine="python")
        pk_column_label = references.get("columns")[0]

        drop_index = self.df[~self.df[fk].isin(pk_table_data[pk_column_label].keys())].index
        if len(drop_index) > 0:
            logger.info(f"{len(drop_index)} rows were deleted, as they did not have matching primary keys.")
            logger.info(f"{len(self.df) - len(drop_index)} rows are left in table as input.")
        self.df = self.df.drop(drop_index)

    def _assign_char_feature(self, feature):
        """
        Assign text based feature to text columns
        """
        max_len, rnn_units = self._preprocess_str_params(feature)
        self.assign_feature(
            CharBasedTextFeature(
                feature, text_max_len=max_len, rnn_units=rnn_units
            ),
            feature,
        )
        logger.debug(f"Feature {feature} assigned as text based feature")

    def _assign_float_feature(self, feature):
        """
        Assign float based feature to float columns
        """
        # num_bins = self.find_clusters(df, float_columns)
        features = self._preprocess_nan_cols(feature, fillna_strategy="mean")
        if len(features) == 2:
            self.null_num_column_names.append(features[1])
        for feature in features:
            self.assign_feature(
                ContinuousFeature(feature, column_type=float), feature
            )
            logger.debug(f"Feature {feature} assigned as float based feature")

    def _assign_int_feature(self, feature):
        """
        Assign int based feature to int columns
        """
        # num_bins = self.find_clusters(df, int_columns)
        features = self._preprocess_nan_cols(feature, fillna_strategy="mean")
        if len(features) == 2:
            self.null_num_column_names.append(features[1])
        for feature in features:
            self.assign_feature(
                ContinuousFeature(feature, column_type=int), feature
            )
            logger.debug(f"Feature {feature} assigned as int based feature")

    def _assign_categ_feature(self, feature):
        """
        Assign categorical based feature to categorical columns
        """
        feature = self._preprocess_categ_params(feature)
        self.assign_feature(CategoricalFeature(feature), feature)
        logger.debug(f"Feature {feature} assigned as categorical based feature")

    def _assign_date_feature(self, feature):
        """
        Assign date feature to date columns
        """
        self.assign_feature(DateFeature(feature), feature)
        logger.debug(f"Feature {feature} assigned as date feature")

    def _assign_binary_feature(self, feature):
        """
        Assign binary feature to binary columns
        """
        feature = self._preprocess_categ_params(feature)
        self.assign_feature(BinaryFeature(feature), feature)
        logger.debug(f"Feature {feature} assigned as binary feature")
    
    def _assign_fk_feature(self):
        """
        Assign corresponding to FK null column and preprocess if required.
        """
        for fk_name, config in self.foreign_keys_mapping.items():
            if "joined_sample" in config and config["joined_sample"]:
                self.__sample_only_joined_rows(fk_name)
            else:
                for fk_column in self.fk_columns:
                    features = self._preprocess_nan_cols(fk_column, fillna_strategy="mode")
                    if len(features) > 1:
                        self.assign_feature(
                            ContinuousFeature(features[1], column_type=int), features[1]
                        )

    def pipeline(self) -> pd.DataFrame:
        columns_nan_labels = get_nan_labels(self.df)
        self.df = nan_labels_to_float(self.df, columns_nan_labels)
        (
            str_columns,
            float_columns,
            categ_columns,
            date_columns,
            int_columns,
            binary_columns,
        ) = data_pipeline(self.df)

        if self.foreign_keys_list:
            self._assign_fk_feature()

            float_columns, int_columns, str_columns, categ_columns = self.__drop_fk_columns(float_columns,
                                                                                            int_columns,
                                                                                            str_columns,
                                                                                            categ_columns)

        self.primary_keys_mapping.update(self.unique_keys_mapping)
        pk_uq_keys_mapping = self.primary_keys_mapping
        if pk_uq_keys_mapping:
            self.__set_types(pk_uq_keys_mapping, str_columns, categ_columns, date_columns)

        for column in self.df.columns:
            if column in str_columns:
                self._assign_char_feature(column)
            elif column in float_columns:
                self._assign_float_feature(column)
            elif column in int_columns:
                self._assign_int_feature(column)
            elif column in categ_columns:
                self._assign_categ_feature(column)
            elif column in date_columns:
                self._assign_date_feature(column)
            elif column in binary_columns:
                self._assign_binary_feature(column)
        
        self.set_nan_params(columns_nan_labels)

        self.fit(self.df)

        return self.df
