# pandas and matplotlib imports
import pandas as pd
import matplotlib.pyplot as plt
# import the csv and store in pandas data fram - changing the names of rows
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
# first 5 rows
df.head()
# rows, columns
df.shape
#column names
df.columns
#last 5 rows
df.tail()


# number of entries in each coloum of the dataframe
df.count()
#number of entrys by programming language
df.groupby("TAG").sum()
# how many months of entries exist in each coloumn
df.groupby("TAG").count()
# print(df.groupby("TAG").count())

# look at second entry in the date column
df["DATE"][1]
#alternative way to look at the date
df.DATE[1]

# what type of data is this ? - string - needs to be a timestamp
type(df["DATE"][1])
# make a dataframe with to_datetime
print(pd.to_datetime(df.DATE[1]))
type(pd.to_datetime(df.DATE[1]))
# now convert the entier date column
df.DATE= pd.to_datetime(df.DATE)
df.head()
print(df.head())
