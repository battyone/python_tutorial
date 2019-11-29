# %%
import seaborn as sn
import json
from collections import Counter
import pandas as pd
import numpy as np

# %%
#########
# load data and create data frame
path = './bitly_usagov.txt'
records = [json.loads(line) for line in open(path)]
df = pd.DataFrame(records)

#############
# clean time zone data
clean_tz = df['tz'].fillna(value='Missing')
clean_tz[clean_tz == ''] = 'Unknown'

#########
# count the various time zones
clean_tz_counts = clean_tz.value_counts()

#########
# display data
subset = clean_tz_counts[:10]
sn.barplot(y=subset.index, x=subset.values)

##############################
# %%
# a key contains Agent strings which can be very long

################
# - split Agent string and remove all but the first part
# - accessing df.a instead of df['a']
# - make a pandas's Serie
a = pd.Series([a.split()[0] for a in df.a.dropna()])
a.value_counts()[:8]

# %%
# copy dataframe?
cframe = df[df.a.notnull()].copy()
cframe['os'] = np.where(cframe['a'].str.contains('Windows'),
                        'Windows', 'Not Windows')

# %%
cframe.os[:8]

# %%
