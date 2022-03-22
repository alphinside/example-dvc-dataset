import pandas as pd
from sklearn.model_selection import train_test_split


class IrisDataset:
    def __init__(self, dataset_path: str = "dataset/iris.csv") -> None:
        self.df = pd.read_csv(dataset_path,index_col=0)

        self.train, self.test = train_test_split(
            self.df, test_size=0.25, random_state=12345
        )
