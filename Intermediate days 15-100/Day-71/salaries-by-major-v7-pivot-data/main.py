import pandas as pd
df = pd.read_csv("salaries_by_college_major.csv")
df.head()
# print(df.shape)
# print(df.columns)
# print(df.isna())
# print(df.tail())
clean_df = df.dropna()

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
# majors by each category
# print(clean_df.groupby('Group').count())
# by mean
# this line cleans up the display to 2 decimals
pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').mean())

