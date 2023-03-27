# Xử lý với file text spam
# Xử lý tương tự với 2 file còn lại


import pandas as pd

content = list()
for i in range(0,18):
    path = str(i)+'_spam.txt'
    with open(path) as f :
        data = f.readlines()
        value = ''
        for x in data:
            x = x.replace('Subject:','')
            if x!='\n':
                x = x.replace('\n','')
                value+=x+' '
        content.append(value)
label = [0 for i in range(18)]
df = pd.Series(content)
df = pd.concat([df,pd.Series(label)],axis=1)
df.columns = ['content','label']
df.to_csv('spam.csv',index=False)