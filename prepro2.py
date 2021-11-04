import pandas as pd 

df = pd.read_csv('result-txt-title-edit.csv')
#print(df.head())

date_ = df['date'][0]
print(date_[:-6])

print(date_[-5:])

date_ = []
time_ = []

for i in df['date']:
    date_.append(i[:-6])
    time_.append(i[-5:])

df['date'] = date_
df['time'] = time_

df.to_csv('result-txt-title-edit1.csv', index=False)