# Define the preprocessing_pipeline
from sklearn.pipeline import Pipeline

from keystrokes.transformers.combined_transformer import CombinedTransformer
from keystrokes.transformers.difference_transformer import DifferenceTransformer
from keystrokes.transformers.transpose_transformer import TransposeTransformer

preprocessing_pipeline = Pipeline(
    [("combined", CombinedTransformer()), ("difference", DifferenceTransformer())]
)


class FeaturePipeline(Pipeline):
    def __init__(self, top_columns=500):
        self.top_columns = top_columns
        steps = [
            ("combined", CombinedTransformer()),
            ("difference", DifferenceTransformer()),
            ("transpose", TransposeTransformer(top_columns)),
        ]
        super().__init__(steps)
