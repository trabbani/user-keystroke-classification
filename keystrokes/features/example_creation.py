import itertools
import random

import numpy as np

from keystrokes.data.data_utils import (
    list_keystroke_files_in_zip,
    random_rows_in_range,
    read_csv_from_zip,
)
from keystrokes.utils.path_utils import ZIP_FILEPATH


class ExampleCreator:
    def __init__(
        self,
        num_observations=5,
        keystrokes_zipfile=ZIP_FILEPATH,
        sampling_start_index=0,
        sampling_end_index=10000,
    ):
        self.num_observations = num_observations
        self.keystrokes_zipfile = keystrokes_zipfile
        self.sampling_start_index = sampling_start_index
        self.sampling_end_index = sampling_end_index

        self.user_file_df = list_keystroke_files_in_zip(self.keystrokes_zipfile)

    def set_sampling_indices(self, sampling_start_index, sampling_end_index):
        self.sampling_start_index = sampling_start_index
        self.sampling_end_index = sampling_end_index

    def read_user_data(self, file_id):
        return read_csv_from_zip(
            self.keystrokes_zipfile, self.user_file_df.loc[file_id, "filename"]
        )

    def random_file_id(self, exclude):
        return random_rows_in_range(
            self.user_file_df,
            N=1,
            start=self.sampling_start_index,
            end=self.sampling_end_index,
            exclude=exclude,
        ).index[0]

    def create_negative_examples(self, file_id):
        # Helper function to divide array into chunks
        def chunks(arr, n):
            return [arr[i : i + n] for i in range(0, len(arr), n)]

        # Helper function to create a dataframe for each pair
        def create_pair_samples(pair):
            return [df[df["TEST_SECTION_ID"].isin(p)] for p in pair]

        # Load user data
        df = self.read_user_data(file_id)

        # Ensure we have enough observations for 3 sets
        unique_obs_ids = df["TEST_SECTION_ID"].unique()
        if len(unique_obs_ids) < self.num_observations * 3:
            raise ValueError(
                f"Insufficient observations. The file should contain at least {self.num_observations * 3} unique observations."
            )

        # Divide observations into three sets and shuffle
        random.shuffle(unique_obs_ids)
        obs_sets = chunks(unique_obs_ids, self.num_observations)

        # Create three combinations
        combinations = list(itertools.combinations(obs_sets, 2))

        # For each combination, create a DataFrame with the corresponding observations
        positive_pairs = [create_pair_samples(pair) for pair in combinations]

        return positive_pairs

    def create_positive_example(self, file_id):
        # Helper function to sample observations from a dataframe
        def sample_observations(df):
            obs_ids = np.random.choice(
                df["TEST_SECTION_ID"].unique(),
                size=self.num_observations,
                replace=False,
            )
            return df[df["TEST_SECTION_ID"].isin(obs_ids)]

        # Load data for the two users and sample observations
        return [
            sample_observations(self.read_user_data(ind))
            for ind in [file_id, self.random_file_id(exclude=file_id)]
        ]

    def create_positive_examples(self, file_id, n_examples=3):
        return [self.create_positive_example(file_id) for _ in range(n_examples)]
