import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class TransposeTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, top_columns=500):
        self.top_columns = top_columns
        self.selected_columns_ = None
        self.transposed_X_ = None

    def fit(self, X, y=None):
        # Apply transpose function
        self.transposed_X_ = self.transpose(X)

        # Calculate column sums
        col_sums = self.transposed_X_.sum()

        # Get the column names with the highest sums
        self.selected_columns_ = col_sums.nlargest(self.top_columns).index.tolist()

        return self

    def transform(self, X, y=None):
        if self.transposed_X_ is not None:
            # Use reindex to select columns, which handles missing columns
            X_transformed = self.transposed_X_.reindex(
                self.selected_columns_, axis=1
            ).reset_index(drop=True)
            self.transposed_X_ = None  # clear the stored dataframe to save memory
            return X_transformed

        return self.transpose(X)

    def transpose(self, dfs, y=None):
        transformed_data = []
        for df in dfs:
            df_melt = df.melt(
                id_vars=["KEYCODE", "NEXT_KEYCODE"],
                value_vars=["ABS_DIFF_PRESS_PRESS_TIME", "ABS_DIFF_HOLD_TIME"],
                var_name="TIME_TYPE",
                value_name="TIME",
            )
            df_melt["BIGRAM_TIME"] = (
                "KEYCODES_"
                + df_melt["KEYCODE"].astype("str")
                + "_"
                + df_melt["NEXT_KEYCODE"].astype("str")
                + "_"
                + df_melt["TIME_TYPE"]
            )
            df_pivot = (
                df_melt.pivot(columns="BIGRAM_TIME", values="TIME")
                .reset_index(drop=True)
                .sum()
                .to_frame()
                .T
            )
            df_pivot.columns = df_pivot.columns.get_level_values(0)
            df_pivot.columns.name = None
            if self.selected_columns_:
                df_pivot = df_pivot.reindex(self.selected_columns_, axis=1)
            transformed_data.append(df_pivot)

        if self.selected_columns_ is not None:
            return (
                pd.concat(transformed_data, axis=0)
                .reindex(self.selected_columns_, axis=1)
                .reset_index(drop=True)
            )
        return pd.concat(transformed_data, axis=0).reset_index(drop=True)
