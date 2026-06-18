import pandas as pd
import numpy as np

#constructing series from a dictionary with an index specified
d = {"a":1,"b":2,"c":3}
ser = pd.Series(data=d,index=["a","b","c"])
print(ser)


#the keys of the dicitionary match with the index values,
#hence the index values have no effect
ser1 = pd.Series(data=d,index=["x","y","z"])
print(ser1)

#constructing series from a list with copy=false
r = [1,2]
ser = pd.Series(r,copy=False)
ser.iloc[0] = 999
print(r)
print(ser)

#constructing series from a 1d ndarray with copy=false
r1 = np.array([1,2])
ser1 = pd.Series(r,copy=False)
ser1.iloc[0] = 999
print(r1)
print(ser1)
