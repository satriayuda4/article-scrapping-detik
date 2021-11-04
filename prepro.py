import pandas as pd
import string

df = pd.read_csv('result-txt-title.csv', encoding='utf8')

title_ = []

for i in df['title']:
    title_.append(i.strip())

df['title'] = title_
df.to_csv('result-txt-title-edit.csv', index=False)