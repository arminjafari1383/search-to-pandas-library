import numpy as np
import pandas as pd

#constructing dataframe from a dictionary
d = {"col1": [1,2],"col2":[3,4]}
df = pd.DataFrame(data=d)
# print(df)


#notice that the inferred dtype is int64
y1 = df.dtypes
# print(y1)

#to enforce a single dtype
df = pd.DataFrame(data=d,dtype=np.int8)
y2 = df.dtypes
# print(y2)


#constructing dataframe from a dictionary including series
d = {"col1":[0,1,2,3], "col2":pd.Series([2,3],index=[2,3])}
y3 = pd.DataFrame(data=d,index=[0,1,2,3])
# print(y3)

#constucting dataframe from numpy ndarray
df2 = pd.DataFrame(
    np.array([[1,2,3],[4,5,6],[7,8,9]]),columns=["a","b","c"]
)
# print(df2)


#constructing dataframe from a numpy ndarray that has labeled columns

data = np.array(
    [(1,2,3),(4,5,6),(7,8,9)],
    dtype=[("a","i4"),("b","i4"),("c","i4")],
)
df3 = pd.DataFrame(data,columns=["c","a"])
# print(df3)


#constructing dataframe from dataclass
from dataclasses import make_dataclass
Point = make_dataclass("Point",[("x",int),("y",int)])
y4 = pd.DataFrame([Point(0,0),Point(0,3),Point(2,3)])
# print(y4)

#constructing dataframe from series/dataframe
ser = pd.Series([1,2,3],index=["a","b","c"])
df = pd.DataFrame(data=ser,index=["a","c"])
# print(df)

df1 = pd.DataFrame([1,2,3],index=["a","b","c"], columns=["x"])
df2 = pd.DataFrame(data=df1,index=["a","c"])
print(df2)

