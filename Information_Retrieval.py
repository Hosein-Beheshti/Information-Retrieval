
import pandas as pd
import numpy as np
import codecs
import sys


def read_dataset(path, name):
    df = pd.read_excel(path + name)
    return df

def tokenize(doc):
    array_tokens = doc.split()
    return array_tokens


df = read_dataset("datasets/", "IR_Spring2021_ph12_7k.xlsx")

content = df.content

tokens = []
for i in range(0, content.size):
    doc = content[i].encode('utf8')
    tokenized_doc = tokenize(doc)
    for token in tokenized_doc:
        temp = []
        temp.append(token)
        temp.append(df.id[i])
        tokens.append(temp)

print(tokens)

for i in tokens:
    sys.stdout.buffer.write(tokenize(i)[0])
    sys.stdout.buffer.write(tokenize(i)[1])



    
    

print(tokenize(doc))
sys.stdout.buffer.write(tokenize(doc)[1])
