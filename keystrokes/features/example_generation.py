from joblib import Parallel, delayed
from sklearn.utils import shuffle

from keystrokes.features.example_creation import ExampleCreator


class ExampleGenerator:
    def __init__(self, creator: ExampleCreator, num_users, first_user_id):
        self.creator = creator
        self.num_users = num_users
        self.first_user_id = first_user_id

    def _process_user(self, user_id):
        p = self.creator.create_positive_examples(user_id)
        n = self.creator.create_negative_examples(user_id)
        return p, n

    def generate(self):
        results = Parallel(n_jobs=-1)(
            delayed(self._process_user)(user_id)
            for user_id in range(
                self.first_user_id, self.first_user_id + self.num_users
            )
        )
        all_p = []
        all_n = []
        for res in results:
            all_p.extend(res[0])
            all_n.extend(res[1])

        X, y = shuffle(all_p + all_n, [1] * len(all_p) + [0] * len(all_n))
        return X, y
