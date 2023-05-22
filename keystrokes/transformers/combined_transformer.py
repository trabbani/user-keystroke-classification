from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

from keystrokes.transformers.key_code_median_transformer import KeyCodeMedianTransformer
from keystrokes.transformers.keyboard_event_transformer import KeyboardEventTransformer


class CombinedTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.pipeline = Pipeline(
            [
                ("keystroke", KeyboardEventTransformer()),
                ("median", KeyCodeMedianTransformer()),
            ]
        )

    def fit(self, X, y=None):
        # Fit is called on each individual pipeline
        for df_pair in X:
            self.pipeline.fit(df_pair[0])
            self.pipeline.fit(df_pair[1])
        return self

    def transform(self, X, y=None):
        transformed_data = []
        for df_pair in X:
            result1 = self.pipeline.transform(df_pair[0])
            result2 = self.pipeline.transform(df_pair[1])
            result_pair = [result1, result2]
            transformed_data.append(result_pair)
        return transformed_data
