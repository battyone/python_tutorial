#%%

import os
import json

JSON = ".\osconfeed.json"

def load():
    if not os.path.exists(JSON):
        raise RuntimeError('JSON does not exist')

    with open(JSON) as fp:
        return json.load(fp)

#%%
feed = load()

#%%
print(type(feed))
print(feed.keys())
print(sorted(feed['Schedule'].keys()))

for k,v in feed['Schedule'].items():
    print(f'{k}: {len(v):3}')