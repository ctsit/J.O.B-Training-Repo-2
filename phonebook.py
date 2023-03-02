import pandas as pd

df = pd.read_csv('phonebook.csv')
df.sort_values(by='last_name', inplace=True)
df.to_csv('newphonebook.csv', index=False)
