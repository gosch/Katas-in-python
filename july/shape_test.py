# importing pandas module
import pandas as pd
import math


# making data frame
from pandocfilters import Math

data = pd.read_csv("https://cdncontribute.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dataframe.size
size = data.size

# dataframe.shape
shape = data.shape

# dataframe.ndim
df_ndim = data.ndim

# series.ndim
series_ndim = data["Salary"].ndim

# printing size and shape
# print("Size = {}\nShape ={}\nShape[0] x Shape[1] = {}".
#       format(size, shape, shape[0] * shape[1]))


df['V']=df['Z7'] -[math.exp(x]) for x in df['VFACT']]


# printing ndim
# print("ndim of dataframe = {}\nndim of series ={}".
#       format(df_ndim, series_ndim))