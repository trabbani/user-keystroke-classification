import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class DifferenceTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        transformed_dataframes = []
        for df_pair in X:
            transformed_df = self.transform_dataframe_pair(df_pair)
            transformed_dataframes.append(transformed_df)
        return transformed_dataframes

    @staticmethod
    def transform_dataframe_pair(df_pair):
        df1, df2 = df_pair
        merged_df = pd.merge(
            df1, df2, on=["KEYCODE", "NEXT_KEYCODE"], suffixes=("_df1", "_df2")
        )
        merged_df["ABS_DIFF_PRESS_PRESS_TIME"] = abs(
            merged_df["MEDIAN_PRESS_PRESS_TIME_df1"]
            - merged_df["MEDIAN_PRESS_PRESS_TIME_df2"]
        )
        merged_df["ABS_DIFF_HOLD_TIME"] = abs(
            merged_df["MEDIAN_HOLD_TIME_df1"] - merged_df["MEDIAN_HOLD_TIME_df2"]
        )
        return merged_df[
            [
                "KEYCODE",
                "NEXT_KEYCODE",
                "ABS_DIFF_PRESS_PRESS_TIME",
                "ABS_DIFF_HOLD_TIME",
            ]
        ]