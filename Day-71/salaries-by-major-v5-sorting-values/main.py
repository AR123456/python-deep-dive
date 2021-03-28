import pandas as pd
df = pd.read_csv("salaries_by_college_major.csv")
df.head()
# print(df.shape)
# print(df.columns)
# print(df.isna())
# print(df.tail())
clean_df = df.dropna()
#the diff between 2 salaries
# print(clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary'])
# # subtraction
# print(clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary']))
# ## insert result of this subtraction as a new column in position 1
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
# print(clean_df.head())

low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())