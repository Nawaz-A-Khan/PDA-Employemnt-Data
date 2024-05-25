import pandas as pd

# Create some example dataframes
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f']})

# Create a dictionary to store the dataframes with keys
dataframes_dict = {'df1': df1, 'df2': df2}

# Now you can access the dataframes by their keys
selected_df = dataframes_dict['df1']
print(selected_df)
df1.plot()