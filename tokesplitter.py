# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:25:29 2016

authors - Robert, Olja and Lenja

"""

import re 
import bs4

#ttext = open('tekist.txt', 'r', encoding = 'utf-8' )


#text =ttext.read().replace('\n','')
#text = bs4.BeautifulSoup(text, 'lxml').get_text()


# СПИСОК АББРЕВИАТУР
abblist = [' Тов.',' тов.',' Mr.',' Ms.',' Mrs.', ' St.']
#

def sentencize(tt):
    sentokens = []


    
    #
    # Осмысленно решить проблему с иницалами, на наш взгляд, можно только
    # с помощью выделения имен. сущностей
    

    sencash = tt
    
    for i in abblist:
        rgx = i[:-1] + 'symbolspeciale'
        sencash = re.sub(i,rgx,sencash)
    
    #texttype-specific
    sencash = re.sub('\[[0-9]*\]','',sencash)
    #
    
    #убираем множественные пробелы
    sencash = re.sub(' {2,}',' ',sencash)
    #
    
    
   
    sentokens = re.split('(?<=[\.\?\!\;])[\W](?=[A-Z0-9А-Я])', sencash)
    for index, m in enumerate(sentokens):
        for i in abblist:
            rgx = i[:-1]+'symbolspeciale'
         
            if rgx not in m:
                continue
            t = re.sub(rgx,i,m)
     
            sentokens[index] = t
    return sentokens

def tokenize(tt):


# C БЭКСЛЕШАМИ У ПИТОНА ЛИЧНЫЕ ТРУДНОСТИ, УВЫ
    tokens = re.findall('[\w]+[\-\—\.\,/]*[\w]+[\-\[\]\—\.\,/]*[\w]+|[\w]+[\-\[\]\—\.\,/]*[\w]+|[\w]+', tt)

    for ind, m in enumerate(tokens):
        for i in abblist:
            if m not in i:
                continue
            else:
                tokens[ind+1] = m  + '. ' + tokens[ind+1]
                break
            
        
    return tokens

#ttext.close()
