# -*- coding: utf-8 -*-

#PRISTAVKI POSLE SUFFIXIS



from nltk.stem import snowball as stem
import time
import pymystem3

mstm = pymystem3.Mystem()

vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

mistakes = []
text = open('mistakes.txt', 'r') 
for line in text:
    line = line.split()
    lc = ''
    for i in line:
        
        if i[0] != '(':
            lc = lc + i + ' '
        else:
            break
    mistakes.append(lc.replace(',','').split())
text.close()
    
mistakes2 = []

mist = open('testset.txt','r',encoding = 'utf-8')

for line in mist:
    mistakes2.append(line.replace('\n',''))

mist.close()
stmr = stem.RussianStemmer()

# for item in mistakes:
 #   cash = []
 #   for word in item:
 #       cash.append(stmr.stem(word))
#    print(cash)


grStoplist = ['CONJ','INTJ','PART','PR','SPRO']
grGolist = ['']

class kuznec:

    worddict = {}
    rootdict = []
    interfixlist = []
    
    cashline = []
    
    with open('umorphodict2.csv', 'r', encoding = 'utf-8') as slovar:
        next(slovar)
    
        for line in slovar:
            line = line.split('\t')
            if line[0] not in worddict:
                worddict[line[0]] = {}  
    
            worddict[line[0]].update({line[3] : {'morph' : line[1], 'status' : line[2], 'place' : line[3], 'allo' : line[4].split('|'), 'pos' : line[5].replace('\n','')}})
            if line[2] == 'корень':
                rootdict.append(line[1])
            if line[2] == 'интерфикс':
                interfixlist.append(line[1])
                
    
#        cashline = [line[0]]
#        if tuple(line[2],line[1]) not in cash:
#            cash.append(tuple(line[2],line[1]))
            
kuzdra = kuznec()
rootdict = list(set(kuzdra.rootdict))
interfixlist = list(set(kuzdra.interfixlist))



                
            
    
        



#wcash = []        
#for word in worddict:
#    
#    l = len(worddict[word])
#    for pl in range(1,l):
#        try:
#            if worddict[word][str(pl)]['status'] == 'суффикс':
#                wcash.append(worddict[word][str(pl)]['morph'])
#        except:
#            print('boink!')
#            pass
#    mrph = set(wcash)



# print(stmr.stemmmm('изменяющимися'))

def Carthes(*args):
  
    if not args:
        return iter(('',))
        
    for i in args:
        return[str(c) + str(b)
               for c in i
               for b in Carthes(*args[1:])]


# VSE KAKIE EST SUFFIXI NA KONCE ZAPISIVAET
class get_sfx():
    sfxs = []

    sfxcash = []
    sfxdict = {}
    sfx2ndordercash = []
    flag = False 
    def sfx2ndorder(self, text, suffix):
        #print(suffix)
        for i in suffix:
            #print(i)
            cart = Carthes(self.sfxs,[i])
            #print(cart[:10])
            for m in cart:
                if text.endswith(m):
                    self.sfxcash.append(m)
                    self.sfx2ndordercash.append(m)
                    self.sfxdict[m] = [m[:len(m) - len(i)], i]
                    #print('суффикс ДВОЙНОЙ ' + m + ' ss ' + i +' !!!')
                    self.flag = True
    def sfx3dorder(self,text,suffix):
        for i in suffix:
            cart = Carthes(self.sfxs,[i])
            for m in cart:
                if text.endswith(i):
                    self.sfxcash.append(m)
                    self.sfxdict[m] = [m[:len(m) - len(i)]] + self.sfxdict[i]
            
    def __init__(self, text, suffix):
        self.sfxcash = []
        self.sfxdict = {}
        self.sfx2ndordercash = []
        self.flag = False
        self.sfxs = []
        self.sfxs = suffix
        for i in suffix:
#        print(i)
            if text.endswith(i):
                self.sfxcash.append(i)
                self.sfxdict[i] = [i]
                #print('суффикс ' + i + ' !!!')
       
        if len(self.sfxcash) > 0:
            #print(self.sfxcash, text)
            self.sfx2ndorder(text, self.sfxcash)
        #if self.flag:
       #     self.sfx3dorder(text,self.sfx2ndordercash)
#        return(self.sfxcash)
    
def strip_end(text, suffix, scheck = 0):
  
    vowelcount = 0
#    i = max(get_sfx(text, suffix), key = len)
    for s in vowels:
        vowelcount = vowelcount +  text[:len(text)-len(suffix)].count(s)
    
    if scheck == 1:    
        if vowelcount > 0 :
            return(text[:len(text)-len(suffix)])
            
                    
        else:
            print('VOWELCOUNT INSUFFICIENT')
            return([text,''])   
    else:
        return(text[:len(text)-len(suffix)])
        
                
#def get_pr(text,prst):
#    prcash = []
#    for i in prst:
#        if text.startswith(i):
#            print('Приставка ' + i + ' !!!')
#            prcash.append(i)
            
class prefixwork:
    
    
    
    def get_prefix(self, text, prst):
        self.prefixlist = ['']
        
        for i in prst:
            if text.startswith(i):
                #print(' CLASSNAJA Приставка ' + i + ' !!!')
                vowelcount = 0
                for s in vowels:
                    
                    vowelcount = vowelcount + text[len(i):].count(s)
                self.vowelcount = vowelcount
                if vowelcount > 0:
#                    ostatok = text[len(i):]
                    self.prefixlist.append(i)
    def strip_start(self):
        if len(self.prefixlist) > 0:
            self.maxprefix = max(self.prefixlist, key = len)
        
    
    def __init__(self, text, prst = stmr.gtprst()):
        self.get_prefix(text, prst)
        self.strip_start()
    
        if len(self.prefixlist) > 0:
            self.ostatok = text[len(self.maxprefix):]
        else:
            self.ostatok = text
            self.maxprefix = ''
        
class postfixwork:
    def get_postfix(self, text, post):
        self.postfixlist = ['']
        
        for i in post:
            if text.endswith(i):
                print(' CLASSNAJA okon4anie ' + i + ' !!!')
                vowelcount = 0
                for s in vowels:
                    
                    vowelcount = vowelcount + text[:len(text)-len(i)].count(s)
                self.vowelcount = vowelcount
                if vowelcount > 0:
#                    ostatok = text[len(i):]
                    self.postfixlist.append(i)
    def strip_end(self):
        if len(self.postfixlist) > 0:
            self.maxpostfix = max(self.postfixlist, key = len)
            
    def __init__(self, text, post = stmr.gtpost()):
        self.get_postfix(text, post)
        self.strip_end()
    
        if len(self.postfixlist) > 0:
            self.ostatok = text[:len(text)-len(self.maxpostfix)]
        else:
            self.ostatok = text
            self.maxpostfix = ''
    
    

                
def get_syll(word):
    vcnt = 0
    for ind, s in enumerate(word):
        if s in vowels:
            vcnt = vcnt + 1
        if vcnt > 1:
            return(word[:ind])
    vcnt = 0
    return(word)
    
    
    
#def recheck(word):
#    print('RECHECK WITH PRSYLL IS BEING RUN')
#    print(word)
#    if word in rootdict:
#        print('STRIKE WORD')
#        return((word,1))
# A-ROOT STEP -----------------------------------------------------------------
#    if word.endswith('а'):
#        arootDict = []
#        for i in stmr.gtart():
#            if word.endswith(i):
#                arootDict.append(i)
#        if len(arootDict) > 0:
#            maxARoot = (max(arootDict, key = len))
#            prst = word[:len(word) - len(maxARoot)]
#            if prst in stmr.gtprst(): 
#                print('STRIKE A-ROOT')
#                return([maxARoot, prst, ''],5)
#
#    nopr = prefixwork(word)
#    if nopr.ostatok in rootdict:
#        print('STRIKE SOLO PR')
#        return([nopr.ostatok, nopr.maxprefix, ''],2)
#    sfxrtcash = {}
#    for i in get_sfx(word, stmr.gtsfx()):
#        if strip_end(word, i) in rootdict:
#            sfxrtcash.update({strip_end(word, i) : i})
#    if len(sfxrtcash) > 0 :
#        maxkey = (max(list(sfxrtcash.keys()), key = len))
#        return([maxkey, '', sfxrtcash[maxkey]],3)
#    if ((len(sfxrtcash) == 0) and (nopr.maxprefix != '')):
#        for i in get_sfx(nopr.ostatok, stmr.gtsfx()):
#            if strip_end(nopr.ostatok, i) in rootdict:
#                sfxrtcash.update({strip_end(nopr.ostatok, i) : i})
#    if len(sfxrtcash) > 0:
#        print('SUTORAIKU SFX!')    
#        maxkey = (max(list(sfxrtcash.keys()), key = len))
#        return([maxkey, nopr.maxprefix, sfxrtcash[maxkey]],3)

class goThroughWord():
    def go_get_it(self,word):
        self.successCode = True
        action_done = None
        RSroot = ['']
        RPSroot = ['']
# FIRST STEP ------------------------------------------------------------------    
# CHECK IF THATS ROOT
        if word in rootdict:

            print('STRIKE WORD')

            self.root += [word]
            return
# A-ROOT STEP -----------------------------------------------------------------
        if self.word.endswith('а'):
            arootDict = []
            for i in stmr.gtart():
                if word.endswith(i):
                    arootDict.append(i)
            if len(arootDict) > 0:
                maxARoot = (max(arootDict, key = len))
                prst = word[:len(word) - len(maxARoot)]
                if prst in stmr.gtprst(): 
                    print('STRIKE A-ROOT')
                    self.prefix += [prst]
                    self.root += [maxARoot]
                    return
# SECOND STEP -----------------------------------------------------------------
# PREFIX + ROOT
        nopr = prefixwork(word)

        self.nopr = nopr
        if nopr.ostatok in rootdict:
            print('STRIKE SOLO PREFIX')
            self.root += [nopr.ostatok]
            self.prefix += [nopr.maxprefix]
            return
# THIRD STEP ------------------------------------------------------------------
        sfxrtcash = {}
        sfxrtcash2 = {}
        action_done = get_sfx(word, stmr.gtsfx())
        
        #print(list(set(action_done.sfxcash)))
        for i in list(set(action_done.sfxcash)):
            #print(i)
            if strip_end(word, i) in rootdict:
                #print('da '+strip_end(word, i))
                sfxrtcash.update({strip_end(word, i) : i})
        self.sfxrtcash = sfxrtcash
#root + single suffix
        if len(sfxrtcash) > 0 :
            maxkey = (max(list(sfxrtcash.keys()), key = len))
            #self.root += [maxkey]
            #self.suffix += [action_done.sfxdict[sfxrtcash[maxkey]]]
            RSroot = [maxkey]
            RSsuffix = [sfxrtcash[maxkey]]
            #print(sfxrtcash)
            print('STRIKE SOLO SUFFIX')
            #return
# root + prefix + suffix
#        if ((len(sfxrtcash) == 0) and (nopr.maxprefix != '')):
        action_done = get_sfx(nopr.ostatok, stmr.gtsfx())
        #print(list(set(action_done.sfxcash)))
        for i in list(set(action_done.sfxcash)):
            if strip_end(nopr.ostatok, i) in rootdict:
                sfxrtcash2.update({ strip_end(nopr.ostatok, i) : i })
        #print(sfxrtcash)
        if len(sfxrtcash2) > 0:
            #print('SUTORAIKU SFX!')    
            maxkey = (max(list(sfxrtcash2.keys()), key = len))
            #print(sfxrtcash2)
            RPSroot = [maxkey]
            RPSprefix = [nopr.maxprefix]
            RPSsuffix = [sfxrtcash2[maxkey]]
            #print(action_done.sfxdict)
            
           
            if (len(RPSroot[0]) >= len(RSroot[0])) :
                #print(RPSroot,RSroot)
                print('ding')
                self.root = RPSroot
                self.prefix = RPSprefix
                self.suffix = RPSsuffix
            else:
                print('dong')
                self.root = RSroot
                self.suffix = RSsuffix
            return
        if len(sfxrtcash) > 0:
            self.root = RSroot
            self.suffix = RSsuffix 
            return
            #self.root += [sfxrtcash[maxkey]]
            #self.prefix += [nopr.maxprefix]
            #self.suffix += [action_done.sfxdict[maxkey]]
            #return

        self.successCode = False
        return 
    def __init__(self,word):
        #self.word = postfixwork(word)    
        #self.postfix = [self.word.maxpostfix]
        self.prefix = []
        self.suffix = []
        self.root = []
        self.nopr = prefixwork('')
        self.second_prefix = []
        self.extraRoot = []
        self.extraSuffix = []
        self.extraPrefix = []
        self.extrasecond_prefix = []
        self.interfix = []
        #self.word = self.word.ostatok
        self.word = word
        print('Fetching basic morphemes... ' + word )
        self.go_get_it(word)


class rootworks():
    
######## DEPRECATED -----------------------------------------------------------
#------------------------------------------------------------------------------
    
#    def go_get_it(self,word):
#        self.successCode = True
 #       
# FIRST STEP ------------------------------------------------------------------    
# CHECK IF THATS ROOT
#        if word in rootdict:
#
#            print('STRIKE WORD')
#
#            self.root += [word]
#            return
## A-ROOT STEP -----------------------------------------------------------------
#        if self.word.endswith('а'):
#            arootDict = []
#            for i in stmr.gtart():
#                if word.endswith(i):
#                    arootDict.append(i)
#            if len(arootDict) > 0:
#                maxARoot = (max(arootDict, key = len))
#                prst = word[:len(word) - len(maxARoot)]
#                if prst in stmr.gtprst(): 
#                    print('STRIKE A-ROOT')
#                    self.prefix += [prst]
#                    self.root += [maxARoot]
#                    return
## SECOND STEP -----------------------------------------------------------------
# PREFIX + ROOT
#        nopr = prefixwork(word)
#
#        self.nopr = nopr
#        if nopr.ostatok in rootdict:
#            print('STRIKE SOLO PREFIX')
#            self.root += [nopr.ostatok]
#            self.prefix += [nopr.maxprefix]
#            return
## THIRD STEP ------------------------------------------------------------------
#        sfxrtcash = {}
#        for i in get_sfx(word, stmr.gtsfx()):
#            if strip_end(word, i) in rootdict:
#                sfxrtcash.update({strip_end(word, i) : i})
##root + single suffix
#        if len(sfxrtcash) > 0 :
#            maxkey = (max(list(sfxrtcash.keys()), key = len))
#            self.root += [maxkey]
#            self.suffix += [sfxrtcash[maxkey]]
#            return
## root + prefix + suffix
#        if ((len(sfxrtcash) == 0) and (nopr.maxprefix != '')):
#            for i in get_sfx(nopr.ostatok, stmr.gtsfx()):
#                if strip_end(nopr.ostatok, i) in rootdict:
#                    sfxrtcash.update({strip_end(nopr.ostatok, i) : i})
#        if len(sfxrtcash) > 0:
#            print('SUTORAIKU SFX!')    
#            maxkey = (max(list(sfxrtcash.keys()), key = len))
#            print(sfxrtcash)
#            self.root += [maxkey]
#            self.prefix += [nopr.maxprefix]
#            self.suffix += [sfxrtcash[maxkey]]
#            return
#
#        self.successCode = False
#        return 

#---------------------------------------------------------------------------
########## DEPRECATED------------------------------------------------------
        
#    def flush(self):
#        self.prefix = []
#        self.suffix = []
#        self.root = []
#
#        self.interfix = []
#    
#    def fetch_decorator(self, dec_fn):
#        def calm_pliz():
#            cashPrefix = self.prefix
#            cashSuffix = self.suffix 
#            cashRoot = self.root
#            self.prefix = []
#            self.suffix = []
#            self.root = []
#            dec_fn()
#            self.currPrefix = self.prefix
#            self.currSuffix = self.suffix
#            self.currRoot = self.root
#            self.prefix = cashPrefix
#            self.suffix = cashSuffix
#            self.root = cashRoot
        
    def grab(self,results):
        self.prefix = []
        self.suffix = []
        self.root = []
        self.extraRoot = []
        self.extraSuffix = []
        self.interfix = []
        self.second_prefix = results.second_prefix
        self.root = results.root
        self.suffix = results.suffix
        self.prefix = results.prefix
        self.extraRoot = results.extraRoot
        self.interfix = results.interfix
        self.extraPrefix = results.extraPrefix
        self.extrasecond_prefix = results.extrasecond_prefix
        #self.postfix = results.postfix
        #self.word = results.word
        self.successCode = results.successCode
        #word = self.word
        

            
    
    def __init__(self, word):
        self.word = postfixwork(word)    
        self.postfix = [self.word.maxpostfix]
        self.prefix = []
        self.second_prefix = []
        self.extraSuffix = []
        self.suffix = []
        self.root = []
        self.extraRoot = []
        self.interfix = []
        self.extraPrefix = []
        self.extrasecond_prefix = []
        self.word = self.word.ostatok
        word = self.word
# FIRST ITERATION
#        self.go_get_it(word)
        self.firstResult = goThroughWord(word)
        #self.grab(self.firstResult)
       # print('adasdasdasd' + self.root + self.prefix + self.postfix + self.suffix)
        
# ADDITIONAL PREFIX
        self.secondResult = goThroughWord(self.firstResult.nopr.ostatok)
        self.secondResult.second_prefix = [self.firstResult.nopr.maxprefix]
        #if not self.successCode:
            
        self.grab(self.secondResult)
        
        
        
# MULTI-ROOT
        def multiroot(warudo):
            
            print('IWEM MNOGO ROOT')
#            self.flush()
            rootCash = []
            for i in rootdict:
                if warudo.startswith(i):
                    rootCash.append(i)
            print(rootCash)
            if len(rootCash)>0:
                #self.extraRoot += [max(list(rootCash), key = len)]
                warudo = warudo[len(max(list(rootCash), key = len)):] # TAK NADO, POVER'.
                                       
                print(warudo)
              #  self.go_get_it(word)
              
                basicResult = goThroughWord(warudo)
                basicResult.extraRoot += [max(list(rootCash), key = len)]
                #self.go_get_it(word)
                self.grab(basicResult)
                root_no_int = ''.join(basicResult.root)
                root_int = ''
                print('DA ETO ON'+root_no_int)
                
                for i in interfixlist:
                    
                    if warudo.startswith(i):
                        print(i)
                        #self.flush()
                        #self.interfix += [i]
                        warudo = warudo[len(i):]
                        basicResult2 = goThroughWord(warudo)
                        self.grab(basicResult2)
                        basicResult2.extraRoot += [max(list(rootCash), key = len)]
                        basicResult2.interfix += [i]
                        #basicResult2.
                        #self.go_get_it(word)
                        root_int = ''.join(basicResult2.root)
                        print('da eto on '+root_int)
                        print('SHOWDOWN - ' + root_no_int + ' ' + root_int)
                    if len(root_int) >= len(root_no_int) and len(root_int) > 0:
                        print('subzero wins')
                        return(basicResult2)
                        #self.root = [root_int]
                        pass
                    else:
                        print('ne wins')
                        return(basicResult)
                            #self.root = [root_no_int]
                            #aself.interfix = []
            
        
        print()
        self.thirdResult = None
        if len(self.firstResult.nopr.maxprefix) >0:
            self.thirdResult = multiroot(self.firstResult.nopr.ostatok)
            if self.firstResult.nopr.maxprefix != None:
                self.thirdResult.extraPrefix = self.firstResult.nopr.maxprefix
        self.fourthResult = None
        if len(self.secondResult.nopr.maxprefix) > 0:
            self.fourthResult = multiroot(self.secondResult.nopr.ostatok)
            if self.secondResult.nopr.maxprefix != None:
               self.fourthResult.extraPrefix = self.firstResult.nopr.maxprefix
               self.fourthResult.extrasecond_prefix = self.secondResult.nopr.maxprefix
        self.fifthResult = multiroot(word)
        return
        
                            
                            
# NUJNA BIG COMBINED STADIA!!!!!!!!!!!!!!!!!!!!!!!!
# UJE NET!!!!!!!!!!!

# MORE PRISTAVKAS
        if not self.successCode:
            
            
            self.prefix += [firstResult.nopr.maxprefix]
            word = firstResult.nopr.ostatok
        
            print('MASS PREFIX STAGE')

            print(self.postfix)
            print(word)
            
            self.prefx = goThroughWord(word)
            #self.go_get_it(word)
            
        return
                   
                    
                    

# MORE SUFFIXES
        if not self.successCode:
            self.prefix += [self.nopr.maxprefix]
            word = self.nopr.ostatok
            suffix = ''
            try:
                suffix = max(get_sfx(word,stmr.gtsfx()), key = len)
                self.suffix += [max(get_sfx(word,stmr.gtsfx()), key = len)]
            except:
                pass
            print(word)
            word = word[:len(word)-len(suffix)]
            print('MAX SUFFIX STAGE')
            print(self.suffix)
            print(word)
            
            self.go_get_it(word)


# IF ALL FAILS        
        if not self.successCode:
            print('MISSION FAILED')
            self.flush()
            try:
                suffix = max(get_sfx(self.word,stmr.gtsfx()), key = len)
                self.suffix += [max(get_sfx(self.word,stmr.gtsfx()), key = len)]
            except:
                pass
            prefix = prefixwork(self.word[:len(self.word)-len(suffix)])
            self.root += [prefix.ostatok]
            self.prefix += [prefix.maxprefix]

            
    
#def get_root(text):
#    global prtr
#    word = postfixwork(text)
#    prtr = word.maxpostfix
#    word = word.ostatok
#    word = stmr.stemmmm(text)[1]
#    prtr = stmr.stemmmm(text)[2][0]
#    print(prtr)
#    print(word)
#    nopr = None
#    print(word)
#    fst = 
#    ffst = strip_end(word, stmr.gtsfx())
#    fnl = strip_start(strip_end(word,stmr.gtsfx())[0],stmr.gtprst())

    
# FIRST STEP ------------------------------------------------------------------    
#    if word in rootdict:
#        print('STRIKE WORD')
#        return((word,1))
# FIRST STEP END --------------------------------------------------------------
# A-ROOT STEP -----------------------------------------------------------------
#    if word.endswith('а'):
#        arootDict = []
#        for i in stmr.gtart():
#            print(i)
#            if word.endswith(i):
#                arootDict.append(i)
#        if len(arootDict) > 0:
#            maxARoot = (max(arootDict, key = len))
#            prst = word[:len(word) - len(maxARoot)]
#            if prst in stmr.gtprst(): 
#                print('STRIKE A-ROOT')
#                return([maxARoot, prst, ''],5)

# SECOND STEP -----------------------------------------------------------------
 #   nopr = prefixwork(word)
 #   if nopr.ostatok in rootdict:
 #       print('STRIKE SOLO PR')
 #       return([nopr.ostatok, nopr.maxprefix, ''],2)
# SECOND STEP END -------------------------------------------------------------
# THIRD STEP ------------------------------------------------------------------
#    sfxrtcash = {}
#    for i in get_sfx(word, stmr.gtsfx()):
#        if strip_end(word, i) in rootdict:
#           sfxrtcash.update({strip_end(word, i) : i})
#    if len(sfxrtcash) > 0 :
#        maxkey = (max(list(sfxrtcash.keys()), key = len))
#        return([maxkey, '', sfxrtcash[maxkey]],3)
#    if ((len(sfxrtcash) == 0) and (nopr.maxprefix != '')):
#        for i in get_sfx(nopr.ostatok, stmr.gtsfx()):
#            if strip_end(nopr.ostatok, i) in rootdict:
#                sfxrtcash.update({strip_end(nopr.ostatok, i) : i})
#    if len(sfxrtcash) > 0:
#        print('SUTORAIKU SFX!')    
#        maxkey = (max(list(sfxrtcash.keys()), key = len))
#        return([maxkey, nopr.maxprefix, sfxrtcash[maxkey]],3)
#   tweakword = word + get_syll(prtr)
#    print('ITO TWEAKWORD - ' + tweakword)
#    twres = recheck(tweakword)
#    if twres != None:
#        return twres
#   
#    mxsfx =  max(get_sfx(word,stmr.gtsfx()), key = len)
#    
##    rezanoe = strip_start(strip_end(word,mxsfx),stmr.gtprst())
#    rezanoe = prefixwork(strip_end(word,mxsfx))
    
#    fnl = [rezanoe.ostatok, rezanoe.maxprefix, mxsfx]
#    print(fnl)
#    print('asdasdsd')
    
#    return(fnl,4)
    
class separator():
           

    def raspil(self, word):
        
        self.redflag = False
        self.reflexiveRemoved = False    # UBIRAEM REFLEXIVE

        word = word.lower()              # lOWERCASE
        self.originalWord = word
        if (word.endswith('ся') or word.endswith('сь'))&(len(word[:len(word)-2])>3):
            word = word[:len(word)-2]
            self.reflexiveRemoved = True
        analyz = mstm.analyze(word)[0]['analysis'][0]['gr']
        self.partofspeech = mstm.analyze(word)[0]['analysis'][0]['gr'].split(',')[0]
        for i in grStoplist:
            if analyz.startswith(i):
                self.redflag = True
                self.root = self.originalWord
                self.separated = self.originalWord
                print('stopword, bailing out')
                return
        self.partofspeech = mstm.analyze(word)[0]['analysis'][0]['gr'][0]
        rslt = rootworks(word)
        self.root = rslt.root
        self.prefix = rslt.prefix
        self.postfix = rslt.postfix
        self.suffix = rslt.suffix
        self.extraRoot = rslt.extraRoot
        self.interfix = rslt.interfix
        self.extraPrefix = rslt.extraPrefix
        self.extrasecond_prefix = rslt.extrasecond_prefix
        self.morphList = []
        self.firstResult = rslt.firstResult
        self.secondResult = rslt.secondResult
        self.thirdResult = rslt.thirdResult
        self.fourthResult = rslt.fourthResult
        self.fifthResult = rslt.fifthResult
        self.morphList += self.extraRoot + self.interfix + self.prefix + self.root + self.suffix+ self.postfix
        
        if self.reflexiveRemoved:
            self.reflexive =  self.originalWord[-2:]
            self.morphList += [self.reflexive]
            
        self.separated = ':'.join(self.morphList)
        self.enumerated = []
        
        for i,m in enumerate(self.morphList):
            self.enumerated.append((m,i))
    def assemble(self):
        self.morphList = []
        self.morphList += self.extraRoot + self.interfix + self.second_prefix + self.prefix + self.root + self.suffix+ self.postfix
        
        if self.reflexiveRemoved:
            self.reflexive =  self.originalWord[-2:]
            self.morphList += [self.reflexive]
            
        self.separated = ':'.join(self.morphList)
        self.enumerated = []
        
        for i,m in enumerate(self.morphList):
            self.enumerated.append((m,i))

    def __init__(self,word):
        self.raspil(word)
    
    
class kuznecFinder(kuznec, separator):
    def notinit(self,root, word = ''):
        if len(word) > 0:
            self.raspil(word)
        root = root[0]
        self.rootdict = {'суффикс' : [], 'префикс' : [], 'интерфикс' : [], 'флексия' : []}
        self.wordlist = []
        for word in self.worddict:
            rootFound = False
            for pos in self.worddict[word]:
                pos = self.worddict[word][pos]
                #print(pos)
                if (pos['status'] == 'корень' and pos['morph'] == root):
                    rootFound = True
#                    print('NAWEL! ' + word)
                    break
            if rootFound:
                self.wordlist.append(word)
                for pos in self.worddict[word]:
                    pos = self.worddict[word][pos]
                    if pos['status'] != 'корень':
                        self.rootdict[pos['status']] += [pos['morph']]
            
                        
        for morph in self.rootdict:
            self.rootdict[morph] = list(set(self.rootdict[morph]))
        #self.root = root
    def matchPos(self, thing, elist = None):
        elist = self.enumerated
        for unit in elist:
            if thing in unit:
                #print(thing)
                #print(unit)
                return(unit)
    def mat(self, morpheme):
        rootNum = self.matchPos(self.root[0])
        morphNum = self.matchPos(morpheme)
#        print(self.root)
#        print(morpheme)
#        print(rootNum)
#        print(morphNum)
        
        delta = rootNum[1] - morphNum[1]
        return([delta,rootNum,morphNum])
    def checkPos(self, morpheme, bundle = None):
        bundle = self.mat(morpheme)
#        print(bundle)
        for word in self.wordlist:
            mPos = None
            rPos = None
            for pos in self.worddict[word]:
                
                posNum = pos
                pos = self.worddict[word][pos]
                
                if (pos['morph'] ==  morpheme)&(pos['status'] == 'суффикс') :
                    mPos = posNum
                if pos['morph'] == self.root[0] :
                    rPos = posNum
            if (mPos != None and rPos != None):
                empDelta = int(rPos) - int(mPos)
                if empDelta == bundle[0]:
                    print('Yeach that is the word - ' + word)
                    return(True)
                    break
        print('MORPHEME SHALL NOT PASS!')
        return(False)



class morphSplitnCheck(kuznecFinder, rootworks):
    def __init__(self,word):
        one_prefix = None
        two_prefix = None
        two_root_no_prefix = None
        self.raspil(word)
        if self.redflag == True:
            return
        self.grab(self.firstResult)
        self.assemble()
        if len(self.suffix) > 0:    
            one_prefix = self.do_check(self.suffix[0])
        self.grab(self.secondResult)
        self.assemble()
        if len(self.suffix) > 0: 
            two_prefix = self.do_check(self.suffix[0])
        if one_prefix:
            self.grab(self.firstResult)
            self.assemble()
            print('odna pristavka')
        elif two_prefix:
            self.grab(self.secondResult)
            self.assemble()
            print('dva pristaka')
        elif (one_prefix == None):
            self.grab(self.firstResult)
            self.assemble()
            print('maybe one')
        elif two_prefix == None:
            self.grab(self.secondResult)
            self.assemble()
            print('maybe two')
        else:
            self.grab(self.secondResult)
            self.assemble()
            #print('nihuja')
            if len(self.fifthResult.suffix) > 0:
                if len(self.fifthResult.suffix[0]) > 0:
                    self.grab(self.fifthResult)
                    self.assemble()
                    self.sfxcash = []
                    
                    for i in stmr.gtsfx():
    #        print(i)
                        if self.suffix[0].startswith(i):
                            self.sfxcash.append(i)
                            #self.sfxdict[i] = [i]
                    for i in Carthes(self.rootdict['суффикс'],self.rootdict['суффикс']):
                        if max(self.sfxcash, key = len) in i: # PROBABLY TUT POMENJAT'!!!!!!!!!!!!1 NA FULL SUFFIX
                            two_root_no_prefix = True
                            #print(two_root_no_prefix)
                            #print(i, max(self.sfxcash, key = len))
            if not two_root_no_prefix:
                print('labmada')
                self.grab(self.firstResult)
                self.assemble()
            else:
                if (len(self.secondResult.root[0]) > len(self.fifthResult.root[0]) + 1)&(len(self.fifthResult.root[0]) < 3):
                    print('labmada')
                    self.grab(self.firstResult)
                    self.assemble()
                    
                    
            
            
            

        
    def do_check(self,morph):
        
        self.notinit(self.root)
        flag = self.checkPos(morph)
        if flag:
            return True
        else: 
            return False


def goThroughCorpus(inp, outputPath):
    csvCash = 'Original\tSeparated\n'
    for item in inp:
        item = item.replace('\n','')
        t = morphSplitnCheck(item)
        csvCash += t.originalWord + '\t' + t.separated.replace('::',':') + '\n'
    dumpling = open(outputPath, 'w', encoding = 'utf-8')
    dumpling.write(csvCash)
    dumpling.close()
        
    



#adict = []    
#for i in kuznec.rootdict:
#    if i.endswith('а'):
#        adict.append(i)
        
#print(set(adict))




#########################
# FUNKTSIA DLYA RAZDELKI NA MORFEMI
# DLYA SAWI
#def get_morphs(wd):
#    wrd = raspil(wd)
#    csh = wrd[2]+':'+':'.join(wrd[1][2])
#    
#    return(list(reversed(csh.split(':'))))

    
#########################

#def finale():
#    dump = open('proverka2.txt','w',encoding = 'utf-8')
#    wcash = ''
#    for i in mistakes:
#        
#        for w in i:
#            try:
#                wrd = raspil(w)
#                wcash = wcash + 'Original : ' + w + '\n' + 'Separated: ' + wrd[2] + '\nSep. full: ' + wrd[2]+':'+':'.join(wrd[1][2]) + '\n\n\n'
#            except:
#                print('4eto powlo ne tak')
#            
#    print(wcash)
 #   dump.write(wcash)
 #   dump.close()
    


#for i in tuple(set(morphdict)):
#    if word.endswith(i):
#        print(strip_end(word,i))