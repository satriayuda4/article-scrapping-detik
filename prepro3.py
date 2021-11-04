import nltk
import pandas as pd
import re #regex library
import string

#nltk.download()
df = pd.read_csv('result-txt-title-edit1.csv')
#print(df.head())

text_ = []

for i in df['text']:
    #case folding
    i = (i.lower())
    #remove angka
    i = re.sub(r"\d+", "", i)
    #remove punctuation
    i = i.translate(str.maketrans("","",string.punctuation))
    #remove whitespace leading & trailing
    i = i.strip()
    #remove multiple whitespace into single whitespace
    i = re.sub('\s+',' ', i)
    text_.append(i)

df['text'] = text_

print(text_[1])

df.to_csv('result-txt-title-edit1-cleaned.csv', index=False)