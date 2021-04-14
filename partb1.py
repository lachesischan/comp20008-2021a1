## Part B Task 1
import re
import os
import pandas as pd
import sys

code_list=[]
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

filepath = 'cricket'
file_list = os.listdir(filepath)


file_directory = ['cricket/'+ s for s in file_list]

for i in sorted(file_directory):
    code(i)


#generate dataframe
data = {"File name":file_list,"Code":code_list}
df = pd.DataFrame (data, columns = ['File name','Code'])
a = sys.argv[-1]
df.to_csv(a)

