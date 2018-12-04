# Philippe Meister
# ENGL/HCI 520
# Final Project 

# import modules 
import os
from glob import glob
from urllib.request import Request
import json, urllib.parse, operator
from collections import Counter

# initiate lists that will be used for corups of words and POS
totalwords=[]
totalpos=[]

# identity POS of interest 
posinput = 'NN'

# for loop through all the individual text files
for fname in glob("*.txt"):
    print(fname)
    f = open(fname, encoding='utf-8', errors='ignore')
    a = f.read()
    a = a.encode('ascii', 'ignore')
    text = a
    f.close()
    
    # connet to stanfor core NLP on Evgeny's server 
    url = 'http://grimm.linguatorium.com:9000'
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, 'expecto', 'patronem')
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
    
    # send text to core NLP and recieve data 
    request = Request(url+'?'+urllib.parse.urlencode({ "properties": '{ "annotators": "tokenize,ssplit,pos", "outputFormat": "json"}' }), text)
    data_received = opener.open(request).read().decode()
    data = json.loads(data_received)
    
    # make lists of words and POS
    d=[]
    for i in range(len(data['sentences'])): 
        d= d + data['sentences'][i]['tokens']
    dwords=[]
    dpos=[]
    for i in d:
        dwords=dwords+[i['word']]
        continue
    for i in d:
        dpos=dpos+[i['pos']]
        continue
    print(dwords)
    print(dpos)
    
    # append to total list 
    totalwords = totalwords + dwords
    totalpos = totalpos + dpos

print(totalwords)
print(totalpos)


# count frequency of occrances in whole corpus 
dict={}
sort_dict={}
for i in range(len(totalpos)):
    if totalpos[i] == posinput:
        if totalwords[i] not in dict.keys():
            dict[totalwords[i]]=1
        else:
            dict[totalwords[i]]+=1
sort_dict=sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
print(sort_dict) 

