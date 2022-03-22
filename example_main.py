from example_dvc_dataset import IrisDataset

dataset = IrisDataset()
print(dataset.train.head())
print(dataset.test.head())