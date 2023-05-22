from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class KeyCodeMedianTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self  # nothing to fit

    def transform(self, X, y=None):
        # Ensure it's a DataFrame
        X = pd.DataFrame(X)

        # Group by KEYCODE and NEXT_KEYCODE, compute median
        X_transformed = (
            X.groupby(["KEYCODE", "NEXT_KEYCODE"])[["PRESS_PRESS_TIME", "HOLD_TIME"]]
            .median()
            .reset_index()
            .rename(
                columns={
                    "PRESS_PRESS_TIME": "MEDIAN_PRESS_PRESS_TIME",
                    "HOLD_TIME": "MEDIAN_HOLD_TIME",
                }
            )
        )

        return X_transformed
