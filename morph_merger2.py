# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:24:57 2017

@author: Robert
"""
import os
import bs4

wordList = []
q = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '\n', '-', '?', '—', '!', '*', '…', ':', '«', '»']

counter = 0
for root, dirs, files in os.walk('E:\\linuxfolder\\rcorp\\texts\\source'):
    for fname in filter(lambda fname: fname.endswith('.xhtml'), files):
        
        document2 = open(os.path.join(root, fname), 'r', encoding = 'utf-8')
        raw_text = bs4.BeautifulSoup(document2.read()).get_text()
        for i in q:
            raw_text = raw_text.replace(i,' ')
        wordList += raw_text.split()
        counter += len(raw_text)
        if counter > 1000000:     
            wordList = list(set(wordList))
            print('Spisok cleared')
            counter = 0
        print(root + fname)
        
        
        

