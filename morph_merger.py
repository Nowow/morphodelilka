# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 03:29:55 2017

@author: Robert
"""


from nltk.stem import snowball as stem
import pickle
import os
import re
stmr = stem.RussianStemmer()

sffx = stmr.gtsfx()

#2-nd order suffixes
sffxList2ndOrder = []
for sfx in sffx:
    for sfx2 in sffx:
        if sfx != sfx2: 
            sffxList2ndOrder += [sfx + sfx2]

#uniqueWords = []
#counter = 0
#for root, dirs, files in os.walk('E:\\linuxfolder\\rcorp\\texts\\source'):
 #           for fname in filter(lambda fname: fname.endswith('.xhtml'), files):
 #               document = open(os.path.join(root, fname), 'r', encoding = 'utf-8')
 #               print('Opened document ' + fname)
 #               cash = re.findall('[А-Яа-я]+',document.read())
 #               for i in cash:
 #                   if i.lower() not in uniqueWords:
 #                       uniqueWords.append(i.lower())
 #                       counter += 1
 #                       if counter % 10000 == 0:
 #                           print(counter)
 #                           print(len(uniqueWords))


corpDump = pickle.load(open('E:\\gitshelter\\morphodelilka\\fullUniqueWordsDumplowercase','rb'))
qwe = {}
for i in corpDump:
    qwe[i] = '1'



#pickleDump = open('E:\\linuxfolder\\pythonworks\\corporaDump', 'rb')

validated2ndorder = []

def goo():
    for i,c in enumerate(sffxList2ndOrder):    
        if c in qwe:
            validated2ndorder.append(c)
        if i % 10 == 0:
            print(i)

def Carthes(*args):
  
    if not args:
        return iter(('',))
        
    for i in args:
        return[str(c) + str(b)
               for c in i
               for b in Carthes(*args[1:])]


#for sfx in sffxList2ndOrder:

#for i in range(10000):
#    for i in sffxList2ndOrder:
        
#    cash = pickle.load(pickleDump)
  