from joblib import Parallel, delayed
from pathlib import Path
from keystrokes.data.data_utils import list_keystroke_files_in_zip
from keystrokes.features.example_creation import ExampleCreator
from keystrokes.utils.path_utils import ZIP_FILEPATH
from keystrokes.pipelines.feature_pipeline import preprocessing_pipeline


class FeatureGenerator:
    """
    This class handles the creation and storage of positive and negative examples from keystroke data.

    """

    def __init__(
        self,
        user_file_df,
        folder_path,
        example_creator: ExampleCreator,
    ):
        self.example_creator = example_creator
        self.user_file_df = user_file_df
        self.folder_path = Path(folder_path)

    def preprocess_and_save_examples(self, user_id, examples, example_type):
        """Preprocess examples and save them."""
        dest_folder = self.folder_path / example_type
        dest_folder.mkdir(parents=True, exist_ok=True)

        for i, df_pair in enumerate(examples):
            features_df = preprocessing_pipeline.transform([df_pair])[0]
            features_df.to_csv(dest_folder / f"{user_id}_{i}.csv", index=False)

    def _generate_examples_and_save(self, row):
        idx = row.Index
        user_id = row.user_id
        if idx % 100 == 0:
            print(f"Processed {idx} users")
        try:
            pos_examples = self.example_creator.create_positive_examples(idx)
            neg_examples = self.example_creator.create_negative_examples(idx)
        except Exception as e:
            print(f"Error creating examples for user_id {user_id}: {e}")
            return None

        self.preprocess_and_save_examples(user_id, pos_examples, "positive")
        self.preprocess_and_save_examples(user_id, neg_examples, "negative")

    def generate(self):
        """Generate and save examples."""
        Parallel(n_jobs=-1)(
            delayed(self._generate_examples_and_save)(row)
            for row in self.user_file_df.itertuples(index=True)
        )


def generate_features(folder_path, start_index=0, end_index=10):
    # Initialize the ExampleCreator and FeatureGenerator
    example_creator = ExampleCreator(
        sampling_start_index=start_index, sampling_end_index=end_index
    )

    user_file_df = list_keystroke_files_in_zip(ZIP_FILEPATH)
    user_file_subset_df = user_file_df.iloc[start_index:end_index]

    feature_generator = FeatureGenerator(
        user_file_df=user_file_subset_df,
        folder_path=folder_path,
        example_creator=example_creator,
    )

    feature_generator.generate()
