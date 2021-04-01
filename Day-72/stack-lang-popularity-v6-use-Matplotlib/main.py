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
# print(df.head())
 ## reshaping the dataframe
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
# print(reshaped_df)
#dimensions of new dataframe
reshaped_df.shape
# columns in the new reshaped dataframe
reshaped_df.columns
#  top 5 rows of reshaped
reshaped_df.head()
# count of the number of entries per language
reshaped_df.count()
#replace NaNs with 0  , the inplace argument means update
reshaped_df.fillna(0, inplace=True)
reshaped_df.head()
# print(reshaped_df.head())
# using the Matplotlib
# supply the horizontal x- values and teh vertica y-vlaues to .plot()
plt.plot(reshaped_df.index, reshaped_df.java)
# same using square bracket notation
plt.plot(reshaped_df.index, reshaped_df['java'])
# resize the chart
plt.figure(figsize=(16,10))
# add labels
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df.java)
#add line for python
plt.plot(reshaped_df.index, reshaped_df.python)
# plot all languages using for loop
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column])