import os
import tarfile
import urllib.request
import pandas as pd
import numpy as np
from zlib import crc32
from pathlib import Path

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets"

HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)

    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)

    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(
        housing_path, "housing.csv")

    return pd.read_csv(csv_path)


def print_hello():
    print("Hello World!")


def say_hello():
    print("Hello World!")


def split_train_test(data, test_ratio=0.2):

    # np.random.seed(42)
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]

    return data.iloc[train_indices], data.iloc[test_indices]


def test_set_check(identifier, test_ratio):
    return (crc32(np.int64(identifier)) & 0xffffffff) < test_ratio * 2 ** 32

# print(test_set_check(2, 0.2))
# a = (crc32(np.int64(2)) & 0xffffffff)
# b = (crc32(np.int64(3)) & 0xffffffff)
# c = test_ratio * 2 ** 32
# print(a)
# print(b)

# print(a<c)
# print(b<c)


def split_train_test_by_id(data, test_ratio, id_column):
    """Return stable set of train and test data"""
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]
