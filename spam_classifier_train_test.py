
import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#code for getting data from email
def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

data = DataFrame({'message': [], 'class': []})

data = data.append(dataFrameFromDirectory('D:\le coding\DataScience-Python3\emails/spam', 'spam'))
data = data.append(dataFrameFromDirectory('D:\le coding\DataScience-Python3\emails/ham', 'ham'))


#-----------------------------------------------------------------------------------------------------
#actual code for spam classifier
#train test
from sklearn.model_selection import train_test_split

train, test = train_test_split(data, test_size=0.2)

vectorizer = CountVectorizer()
tr_counts = vectorizer.fit_transform(train['message'].values)
classifier = MultinomialNB()
tr_targets = train['class'].values
classifier.fit(tr_counts, tr_targets)
#testing
t_counts=vectorizer.transform(test['message'].values)
predictions1 = classifier.predict(t_counts)
correct=0
total=0
i=0
for con in predictions1:
    if con==test['class'].values[i]:
        correct+=1
    total+=1
    i+=1
    
print(float(correct/total))    