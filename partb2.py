# Part B Task 2
import re
import os
import sys

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

filename = sys.argv[-1]
a = slice(7)
name = slice(7,14)

print(preprocessing(filename[a]+'/' + filename[name]))



