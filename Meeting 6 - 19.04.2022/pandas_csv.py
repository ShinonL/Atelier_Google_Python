import pandas as pd
import matplotlib.pyplot as matplot

df = pd.read_csv('pandas_csv.csv')

print('Initial CSV')
print(df)

print('\nGet column values')
for index in df.index:
    print(df.loc[index, 'AL'])

print('\nGet correlations')
print(df.corr())

print('\nGet description')
print(df.describe())

print('\nGet mean')
print(df.mean())

# df.plot(kind='scatter', x='AT', y='BE')
# df['AT'].plot(kind='hist')
# matplot.show()

print('\nReplace NaN with 10 on column AL')
df['AL'].fillna(10, inplace = True)
print(df)

print('\nReplace a value by index and column')
df.loc[7, 'AL'] = 45
print(df)

print('\nReplace a value')
df.replace(': ', 0, inplace = True)
df.replace(':', 0, inplace = True)
print(df)


print('\nGet Transpose')
print(df.transpose())
df.to_csv('cleaned_csv.csv')