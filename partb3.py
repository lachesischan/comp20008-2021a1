## Part B Task 3
import re
import sys
import os 




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
key_word_list = [' '+ i +' ' for i in key_word_list]

file_list = os.listdir('cricket')

for i in sorted(file_list):
    article = preprocessing("cricket/"+ i)
    boolen_list=[]
    for s in key_word_list:
        if re.search(s, article):
            a=1
            boolen_list.append(a)
        else:
            a=0
            boolen_list.append(a)
    if all(boolen_list)== True:
        code('cricket/' + i)

print(code_list)
                        

            
        






