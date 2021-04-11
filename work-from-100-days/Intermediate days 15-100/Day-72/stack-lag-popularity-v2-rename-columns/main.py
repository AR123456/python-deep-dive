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

