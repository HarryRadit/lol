from sklearn import datasets
import numpy as np

digits = datasets.load_digits()
print(type(digits.data))  # Data type of digits.data
print(type(digits.target))  # Data type of digits.target
print(type(digits.images))  # Data type of digits.images
print(type(digits.target_names))  # Data type of digits.target_names

# Get the unique labels in the dataset
unique_labels = digits.target_names.astype(int)
print(unique_labels)
