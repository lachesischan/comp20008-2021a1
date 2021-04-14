## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer


#!/usr/bin/env python
# coding: utf-8

# In[21]:


 




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
    pattern_s = '[A-Z]{4}-\d{3}[A-Z][a-z]'
    
    if re.search(pattern,file_string):
        if re.search(pattern_s,file_string):
            code_list.append(re.findall(pattern, file_string)[0][:-1])
        else:
            code_list.append(re.findall(pattern, file_string)[0])
    else:
        code_list.append('Not Found')










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

print(code_list)
                        

            
        





