import os
import re

path = "../data/"

fname = []
regex = re.compile(r"([0-9]{4})-00-00")
my_path = os.path.abspath(os.path.dirname(__file__))
for root, d_names, f_names in os.walk(path, followlinks=True):
    for f in f_names:
        if f.endswith(".xml"):          
            s = open(os.path.join(my_path, root+"/"+f), mode='r', encoding='utf-8-sig').read()
            s = regex.sub("\g<1>-01-01T00:00:00Z", s)
            open(os.path.join(my_path, root+"/"+f), mode='w', newline='\n', encoding='utf-8').write(s)