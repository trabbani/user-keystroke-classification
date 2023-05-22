from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class KeyboardEventTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, max_press_time=5000):
        self.max_press_time = max_press_time

    def fit(self, X, y=None):
        return self  # nothing to fit

    def transform(self, X, y=None):
        # Ensure it's a DataFrame
        X = pd.DataFrame(X)

        # Sort by PRESS_TIME
        X = X.sort_values(by="PRESS_TIME")

        # Calculate PRESS_PRESS_TIME: this is the time difference between the press events of successive keys
        X["PRESS_PRESS_TIME"] = X["PRESS_TIME"].shift(-1) - X["PRESS_TIME"]

        # Calculate HOLD_TIME: this is the time difference between release time and press time of a key
        X["HOLD_TIME"] = X["RELEASE_TIME"] - X["PRESS_TIME"]

        # Calculate NEXT_KEYCODE: this is the key code of the next key pressed
        X["NEXT_KEYCODE"] = X["KEYCODE"].shift(-1)

        # Drop original columns
        X = X.drop(columns=["PRESS_TIME", "RELEASE_TIME"])

        # Filter rows
        # Remove rows with NaN
        X = X.dropna()

        # Convert NEXT_KEYCODE to int
        X["NEXT_KEYCODE"] = X["NEXT_KEYCODE"].astype(int)

        # Filter out rows with PRESS_PRESS_TIME greater than max_press_time
        X = X[X["PRESS_PRESS_TIME"] <= self.max_press_time]

        # Return the transformed DataFrame
        return X.reset_index(drop=True)[
            [
                "KEYCODE",
                "NEXT_KEYCODE",
                "PRESS_PRESS_TIME",
                "HOLD_TIME",
            ]
        ]
