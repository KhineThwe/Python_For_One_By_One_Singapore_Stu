import pandas as pd


# df = pd.read_excel('file.xlsx')
# print(df)


df = pd.read_excel('file.xlsx',sheet_name='Sheet1',usecols=['A','B','C'])
# df = pd.read_excel('file.xlsx',nrows=100)
# print(df)
#print(df.head())#first 5
print(df.head(7))

