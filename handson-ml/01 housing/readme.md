# Housing dataset

Once the dataset is loaded into a pandas DataFrame it can be examined via:

```
housing.head()
housing.info()
housing.describe()
```

In total there are 20640 lines. Each line has up to attributes. For some rows there are `total_bedrooms` missing.

```
longitude             20640 non-null float64
latitude              20640 non-null float64
housing_median_age    20640 non-null float64
total_rooms           20640 non-null float64
total_bedrooms        20433 non-null float64
population            20640 non-null float64
households            20640 non-null float64
median_income         20640 non-null float64
median_house_value    20640 non-null float64
ocean_proximity       20640 non-null object
```

One of the attributes is an labeled as an object. All values can be listed via:

```
housing["ocean_proximity"].value_counts()
```

Showing the histogram of all numerical attributes:

```
housing.hist(bins=50, figsize(20,15))
```

Pandas `hist()` relies on Matplotlib.

The median_income seems to be in $10K. The mean is 3.87 which should be $38,700.

The _target label_ is "median_house_value" seems to be capped at around $500K. It might be a good idea to purge the rows with $500K, otherwise the ML algo might think that the value is the max.

## Create a Test Set

sklearn has a function to split a data set into train and test. The random_state ensures we always select the same sets. The test size is 20% of the overall set.

```
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
```
