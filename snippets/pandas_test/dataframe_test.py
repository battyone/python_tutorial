#%%
import numpy as np
import pandas as pd

#%%

# M freq is Month End
ts = pd.Series([1,2,3,4], 
    index=pd.date_range('1/1/2000', periods=4, freq='M'))
print(ts)

b = ts.shift(1)
print(b)
