import pandas as pd

data = {
  'Duration':{
    '0':60,
    '1':60,
    '2':60,
    '3':45,
    '4':45,
    '5':60
  },
  'Pulse':{
    '0':110,
    '1':117,
    '2':103,
    '3':109,
    '4':117,
    '5':102
  },
  'Maxpulse':{
    '0':130,
    '1':145,
    '2':135,
    '3':175,
    '4':148,
    '5':127
  },
  'Calories':{
    '0':409,
    '1':479,
    '2':340,
    '3':282,
    '4':406,
    '5':300
  }
}

print('Get data frame')
df = pd.DataFrame(data)
print(df)

print('\nGet first / last x elements (default 5)')
print(df.head(3))
print(df.tail(3))

print('\nGet info about data')
print(df.info())