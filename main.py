import pandas as pd

# train file
df1 = pd.read_csv('notspam.csv')
df2 = pd.read_csv('spam.csv')
df = pd.concat([df1,df2],ignore_index=True)

# test file
df3 = pd.read_csv('unknown.csv')

# Prepare data
X_train = df['content']
y_train = df['label']
X_test = df3['content']

# Convert data to matrix.
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
train_data = cv.fit_transform(X_train)
test_data = cv.transform(X_test)

# Classification
from sklearn.naive_bayes import MultinomialNB

naive_bayes = MultinomialNB()
naive_bayes.fit(train_data,y_train)
y_pred = naive_bayes.predict(test_data)

y_pred = pd.Series(y_pred,name='label')
y_pred.replace({1:'notspam',0:'spam'},inplace=True)
file_name = [str(i)+'_unknown.txt' for i in range(78)]
file_name = pd.Series(file_name)

df_result = pd.concat([file_name,y_pred],axis=1)
df_result.columns = ['file_name','label']

print(df_result.label.value_counts())
df_result.to_csv('label_unknown_file.csv',index=False)
