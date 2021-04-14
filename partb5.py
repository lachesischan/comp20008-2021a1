## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
import sklearn
import math
from sklearn.feature_extraction.text import TfidfTransformer
nltk.download('all')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

code_list = []
def reverse_case(match_obj):
    char_elem = match_obj.group(0)
    if char_elem.islower():
        return char_elem.upper()
    else:
        return char_elem.lower() 


def preprocessing(file_name):
    f = open(file_name)
    file_string = f.read()

#pattern
    pattern = '[^a-zA-Z \\n]+'

    x1 = re.sub(pattern, "", file_string)

    x2 = re.sub("[\s+\\n+]+",' ',x1)

    x3 = re.sub('[A-Z]+', reverse_case,x2)
    return x3



def code(file_name):
    f= open(file_name, encoding="ISO-8859-1")
    file_string =f.read()

    pattern = '[A-Z]{4}-\d{3}[A-Z]?'

    
    return code_list.append(re.findall(pattern, file_string))










key_word_list = sys.argv[1:]
key_word_list_base = []
stem = PorterStemmer()

for i in sorted(key_word_list):
    y = stem.stem(i)
    key_word_list_base.append(y)

key_word_list_base = [' '+ i +' ' for i in key_word_list_base]    

file_list = os.listdir('cricket')

for i in sorted(file_list):
    article = preprocessing("cricket/"+ i)
    article_token = nltk.word_tokenize(article)
    article_token_base = []
    for e in sorted(article_token):
        z = stem.stem(e)
        article_token_base.append(z)
    article_token_base = [' '+ i +' ' for i in article_token_base]
    boolen_list=[]
    for s in sorted(key_word_list_base):
        if s in article_token_base:
            a=1
            boolen_list.append(a)
        else:
            a=0
            boolen_list.append(a)
    if all(boolen_list)== True:
        code('cricket/' + i)



#part5 coding
from partb1 import df

df_select = df[df['Code'].isin(code_list)]
file_list_select = df_select['File name'].tolist()
sw = stopwords.words('english')

article_word_list = []
for i in sorted(file_list_select):
    article = preprocessing("cricket/"+ i)
    article_token  = word_tokenize(article)
    article_token_base = []
    for e in sorted(article_token):
        z = stem.stem(e)
        article_token_base.append(z)
    article_token_nosw = {w for w in article_token_base if not w in sw}
    article_token_nosw.tolist()
    article_word_list.append(article_token_nosw)

word_set = set(article_word_list)


term_counts = []
for i in sorted(file_list_select):
    article = preprocessing("cricket/"+ i)
    article_token  = word_tokenize(article)
    article_token_base = []
    for e in sorted(article_token):
        z = stem.stem(e)
        article_token_base.append(z)
    article_token_nosw = {w for w in articel_token_base if not w in sw}
    counts = []
    for w in sorted(word_set):
        if w in article_token_nosw:
            counts.append(1)
        else:
            counts.append(0)
        
        term_counts.append(counts)

print(term_counts)


transformer = TfidfTransformer()
tfidf = transformer.fit_transform(term_counts)
doc_tfidf = tfidf.toarray()


import numpy
from numpy import dot
from numpy.linalg import norm

def cosine_sim(v1,v2):
    return dot(v1,v2)/(norm(v1)*norm(v2))

query_vector = []
for i in sorted(key_word_list_base):
    if i in article_token_nosw:
        query_vector.append(1)
    else:
        query_vector.append(0)

q_unit = [x/(math.sqrt(3)) for x in query_vector]

sims = [cosine_sim(q_unit,doc_tfidf[d_id])for d_if in range(doc_tfidf.shape[0])]

data_final = {'DocumentID':file_list_select, 'score':sims}
df_final = pd.dataframe(data_final,columns = ['Document','score'])
print(df_final)
                        
          

