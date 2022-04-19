import pandas as pd

print('DataFRame')
dataset = {
    'cars': ['BMW', 'Dacia', 'Ford'],
    'colors': ['red', 'green', 'blue']
}

var = pd.DataFrame(dataset, index=['i1', 'i2', 'i3'])
print(var)

print('\nRetrieve by index')
print(var.loc[['i1', 'i3']])

print('\nSeries')
colors = ['red', 'green', 'blue']
var = pd.Series(colors, index = ['x', 'y', 'z'])
print(var)

print('\nRetrieve by index')
print(var[1])
print(var['y'])

print('\nConvert dictionary to series')
dataset = {'BMW': 'red', 'Dacia': 'green', 'Ford': 'blue'}
var = pd.Series(dataset, index=['BMW', 'Dacia'])
print(var)

print('\nGet max rows of a file')
print(pd.options.display.max_rows)