# -*- coding: utf-8 -*-

#PRISTAVKI POSLE SUFFIXIS



#from nltk.stem import snowball as stem
import morph_container
#import time
import pymystem3
from collections import defaultdict
import operator


def printx(*args):
    #print(args)
    pass

mstm = pymystem3.Mystem()

musor = ['1','2','3','4','5','6','7','8','9','0']
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
"""
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
"""
stmr = morph_container.controller()

# for item in mistakes:
 #   cash = []
 #   for word in item:
 #       cash.append(stmr.stem(word))
#    printx(cash)


grStoplist = ['CONJ','INTJ','PART','PR','SPRO']
grGolist = ['A','ADV','ADVPRO','ANUM','APRO','COM','NUM','S','V']

class kuznec:

    worddict = {}
    rootdict = defaultdict(list)
    interfixlist = []
    suffixdict = defaultdict(list)
    cashline = []
    
    with open('resources/umorphodict2.csv', 'r', encoding = 'utf-8') as slovar:
        next(slovar)
    
        for line in slovar:
            line = line.split('\t')
            if line[0] not in worddict:
                worddict[line[0]] = {}  
    
            worddict[line[0]].update({line[3] : {'morph' : line[1], 'status' : line[2], 'place' : line[3], 'allo' : line[4].split('|'), 'pos' : line[5].replace('\n','')}})
            if line[2] == 'корень':
                for gram in grGolist:
                    if gram in line[5].replace('\n','').split(','):
                        rootdict[gram] += [line[1]]
                        if len(line[4])>0:
                            allom = line[4]
                            for x in musor:
                                allom.replace(x,'')
                            allom = allom.split('|')
                            rootdict[gram]+=allom
            if line[2] == 'суффикс':
                for gram in grGolist:
                    if gram in line[5].replace('\n','').split(','):
                        suffixdict[gram] += [line[1]]
            if line[2] == 'интерфикс':
                interfixlist.append(line[1])
    for i in rootdict:
        rootdict[i] = list(set(rootdict[i]))
    for i in suffixdict:
        suffixdict[i] = list(set(suffixdict[i]))
                
    
#        cashline = [line[0]]
#        if tuple(line[2],line[1]) not in cash:
#            cash.append(tuple(line[2],line[1]))

kuzdra = kuznec()
rootdict = kuzdra.rootdict
suffixdict = kuzdra.suffixdict
interfixlist = list(set(kuzdra.interfixlist))
interfixlist += ['я']



                
            
    
        



#wcash = []        
#for word in worddict:
#    
#    l = len(worddict[word])
#    for pl in range(1,l):
#        try:
#            if worddict[word][str(pl)]['status'] == 'суффикс':
#                wcash.append(worddict[word][str(pl)]['morph'])
#        except:
#            printx('boink!')
#            pass
#    mrph = set(wcash)



# printx(stmr.stemmmm('изменяющимися'))

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
        #printx(suffix)
        for i in suffix:
            #printx(i)
            cart = Carthes(self.sfxs,[i])
            #printx(cart[:10])
            for m in cart:
                if text.endswith(m):
                    self.sfxcash.append(m)
                    self.sfx2ndordercash.append(m)
                    self.sfxdict[m] = [m[:len(m) - len(i)], i]
                    #printx('суффикс ДВОЙНОЙ ' + m + ' ss ' + i +' !!!')
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
#        printx(i)
            if text.endswith(i):
                self.sfxcash.append(i)
                self.sfxdict[i] = [i]
                #printx('суффикс ' + i + ' !!!')
       
        if len(self.sfxcash) > 0:
            #printx(self.sfxcash, text)
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
            printx('VOWELCOUNT INSUFFICIENT')
            return([text,''])   
    else:
        return(text[:len(text)-len(suffix)])
        
                
#def get_pr(text,prst):
#    prcash = []
#    for i in prst:
#        if text.startswith(i):
#            printx('Приставка ' + i + ' !!!')
#            prcash.append(i)
            
class prefixwork:
    
    
    
    def get_prefix(self, text, prst):
        self.prefixlist = ['']
        
        for i in prst:
            if text.startswith(i):
                #printx(' CLASSNAJA Приставка ' + i + ' !!!')
                #vowelcount = 0
                #for s in vowels:
                    
                #    vowelcount = vowelcount + text[len(i):].count(s)
                #self.vowelcount = vowelcount
                #if vowelcount > 0:
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
    def get_postfix(self, text, post, pos = ''):
        self.postfixlist = ['']
        #print(pos)
        for i in post:
            if text.endswith(i):
                #print(i, 'OKON4ANIE')
                #if pos == 'S':
                #    if i == 'ть':
                        #print('BABUDA')
                        
                #        continue
#                
                self.postfixlist.append(i)
    def strip_end(self):
        if len(self.postfixlist) > 0:
            self.maxpostfix = max(self.postfixlist, key = len)
            
    def __init__(self, text, post = stmr.gtpost(), pos = '', sklonenie = False):
        
        if sklonenie == True:
            post = stmr.gtpost_burelom()
        self.get_postfix(text, post, pos = pos)
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
    
    
    
#

class goThroughWord():
    def go_get_it(self,word, PoS):
        self.successCode = True
        action_done = None
        RSroot = ['']
        RSsuffix = ['']
        RPSroot = ['']
        rootdict = kuzdra.rootdict[PoS]
        #printx(rootdict)
# FIRST STEP ------------------------------------------------------------------    
# CHECK IF THATS ROOT
        if word in rootdict:

            printx('STRIKE WORD')

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
                    printx('STRIKE A-ROOT')
                    self.prefix += [prst]
                    self.root += [maxARoot]
                    return
# SECOND STEP -----------------------------------------------------------------
# PREFIX + ROOT
        nopr = prefixwork(word)

        self.nopr = nopr         
            
        if nopr.ostatok in rootdict:
            if (globalCounter>0):
                zzjay.root = [nopr.ostatok]
                zzjay.prefix = [nopr.maxprefix]
                zzjay.partofspeech = PoS
                zzjay.assemble()
                if zzjay.do_check(nopr.maxprefix,'префикс'):
                    printx('STRIKE SOLO PREFIX - prefix:' + nopr.maxprefix +', root: '+ nopr.ostatok)
                    self.root += [nopr.ostatok]
                    self.prefix += [nopr.maxprefix]
                    return
# THIRD STEP ------------------------------------------------------------------
        sfxrtcash = {}
        sfxrtcash2 = {}
        action_done = get_sfx(word, stmr.gtsfx())
        self.action_done = action_done
        #printx(list(set(action_done.sfxcash)))
        for i in list(set(action_done.sfxcash)):
            #printx(i)
            if strip_end(word, i) in rootdict:
                #printx('da '+strip_end(word, i))
                sfxrtcash.update({strip_end(word, i) : i})
        self.sfxrtcash = sfxrtcash
#root + suffix
        if len(sfxrtcash) > 0 :
            maxkey = (max(list(sfxrtcash.keys()), key = len))
            #self.root += [maxkey]
            #self.suffix += [action_done.sfxdict[sfxrtcash[maxkey]]]
            RSroot = [maxkey]
            RSsuffix = [sfxrtcash[maxkey]]
            #printx(sfxrtcash)
            printx('STRIKE SOLO SUFFIX - root: ' + maxkey + ', suffix: ' + sfxrtcash[maxkey])
            #return
# root + prefix + suffix
#        if ((len(sfxrtcash) == 0) and (nopr.maxprefix != '')):
        action_done = get_sfx(nopr.ostatok, stmr.gtsfx())
        #printx(list(set(action_done.sfxcash)))
        for i in list(set(action_done.sfxcash)):
            if strip_end(nopr.ostatok, i) in rootdict:
                sfxrtcash2.update({ strip_end(nopr.ostatok, i) : i })
        #printx(sfxrtcash)
        if len(sfxrtcash2) > 0:
            #printx('SUTORAIKU SFX!')    
            maxkey = (max(list(sfxrtcash2.keys()), key = len))
            #printx(sfxrtcash2)
            RPSroot = [maxkey]
            RPSprefix = [nopr.maxprefix]
            RPSsuffix = [sfxrtcash2[maxkey]]
            #printx(action_done.sfxdict)
            
           
            if (len(RPSroot[0]) >= len(RSroot[0]))&(len(RPSprefix[0])>0) :
                #printx(RPSroot,RSroot)
                printx('ding\nFetching result:', RPSprefix, RPSroot, RPSsuffix)
                if globalCounter>0:
                    zzjay.root = RPSroot
                    zzjay.prefix = RPSprefix
                    zzjay.assemble()
                    if zzjay.do_check(RPSprefix[0],'префикс'):
                        printx('STRIKE SOLO PREFIX - prefix:' + nopr.maxprefix +', root: '+ nopr.ostatok)
                        self.root = RPSroot
                        self.prefix = RPSprefix
                        self.suffix = RPSsuffix
                        return
                    else:
                        printx('dongdong\nFetching result:', RSroot, RSsuffix)
                        self.root = RSroot
                        self.suffix = RSsuffix
                #self.root = RPSroot
                #self.prefix = RPSprefix
                #self.suffix = RPSsuffix
            else:
                printx('dong\nFetching result:', RSroot, RSsuffix)
                self.root = RSroot
                self.suffix = RSsuffix
            return
       # printx(sfxrtcash,sfxrtcash2)
        if len(sfxrtcash) > 0:
            printx('\n Fetching result:', RSroot, RSsuffix)
            self.root = RSroot
            self.suffix = RSsuffix 
            return
            #self.root += [sfxrtcash[maxkey]]
            #self.prefix += [nopr.maxprefix]
            #self.suffix += [action_done.sfxdict[maxkey]]
            #return
        # ALL FAILED, RESORT TO DIRTY TRICKS FOR A FILLER
        for i in range(len(word)):
            truncated = word[:len(word) - i]
            if truncated in rootdict:
                
                RSroot = truncated
                RSsuffix = word[len(word)-i+1:]
                printx('DIRTY TRICKS - ROOT:',RSroot, 'SUFFIX:',RSsuffix)
                self.root = [RSroot]
                self.suffix = [RSsuffix]
                return
            
        #self.root = word[0]
        #self.suffix = word[0:]
        self.successCode = False
        return 
    def __init__(self,word, PoS = 'V'):
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
        printx('Fetching basic morphemes... ' + word )
        self.go_get_it(word, PoS)


class rootworks():
    
    def grab(self,results):
        self.prefix = []
        self.suffix = []
        self.root = []
        self.extraRoot = []
        self.extraSuffix = []
        self.interfix = []
        self.extraPrefix = []
        self.second_prefix = results.second_prefix
        self.root = results.root
        self.suffix = results.suffix
        self.prefix = results.prefix
        self.extraRoot = results.extraRoot
        self.extraSuffix = results.extraSuffix
        self.interfix = results.interfix
        self.extraPrefix = results.extraPrefix
        self.extrasecond_prefix = results.extrasecond_prefix
        #self.postfix = results.postfix
        #self.word = results.word
        self.successCode = results.successCode
        #word = self.word
        

            
    
    def __init__(self, word, PoS, sklonenie):
        self.word = postfixwork(word, pos = PoS, sklonenie = sklonenie)    
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
        rootdict = kuzdra.rootdict[PoS]
        word = self.word
# FIRST ITERATION
#        self.go_get_it(word)
        self.firstResult = goThroughWord(word, PoS)
        #self.grab(self.firstResult)
       # printx('adasdasdasd' + self.root + self.prefix + self.postfix + self.suffix)
        
# ADDITIONAL PREFIX
        self.secondResult = goThroughWord(self.firstResult.nopr.ostatok, PoS)
        self.secondResult.second_prefix = [self.firstResult.nopr.maxprefix]
        #if not self.successCode:
            
        self.grab(self.secondResult)
        
        
        
# MULTI-ROOT
        def multiroot(warudo, PoS):
            
            printx('IWEM MNOGO ROOT for word: '+ warudo, ' PoS: '+PoS)
#            printx(warudo)
#            self.flush()
            rootCash = []
            nFlag = False
            for i in rootdict:
                if warudo.startswith(i):
                    rootCash.append(i)
            #printx(rootCash)
            if len(rootCash) == 0:
                printx('NO MULTIROOTS, BAILING OUT')
                return(goThroughWord('',PoS))
            if len(rootCash)>0:
                #self.extraRoot += [max(list(rootCash), key = len)]
                warudo = warudo[len(max(list(rootCash), key = len)):] # TAK NADO, POVER'.
                printx('SOME EXTRA ROOT FOUND, now word: '+ warudo + ', root: ' + max(list(rootCash), key = len))
               # printx(warudo)
              #  self.go_get_it(word)
                if warudo.startswith('н')|warudo.startswith('к'):
                    letter = warudo[0]
                    warudo = warudo[1:]
                    nFlag = True
                    printx('YERRRR STARTS FROM N')
                #if len(warudo) < 3:
               #     printx('MULTIROOT BAILING OUT, TOO SHORD WORD: '+warudo)
               #     return(goThroughWord('', PoS))
              
                basicResult = goThroughWord(warudo, PoS)
                if nFlag:
                    printx('YERRRRRRRRRRR ADDED N TO SFX')
                    basicResult.extraSuffix += [letter]
                
                printx('GOING FOR WARUDO MORPHEMES')
                basicResult.extraRoot += [max(list(rootCash), key = len)]
                #self.go_get_it(word)
                self.grab(basicResult)
                root_no_int = ''.join(basicResult.root)
                root_int = ''
                printx('PROBABLE ROOT WITHOUT INTERFIX: '+root_no_int)
                printx('TRYING INTERFIXES...')
                for i in interfixlist:
                    printx('I HAVE A WARUDO: ' + warudo + ', I HAVE AN INTERFIX: ' + i)
                    if warudo.startswith(i):
                        printx(i)
                        #self.flush()
                        #self.interfix += [i]
                        warudo = warudo[len(i):]
                        basicResult2 = goThroughWord(warudo, PoS)
                        self.grab(basicResult2)
                        basicResult2.extraRoot += [max(list(rootCash), key = len)]
                        basicResult2.interfix += [i]
                        if nFlag:
                            basicResult2.extraSuffix += [letter]
                        #basicResult2.
                        #self.go_get_it(word)
                        root_int = ''.join(basicResult2.root)
                        printx('PROBABLE ROOT WITH INTERFIX: '+root_int)
                        break
                        #printx('da eto on '+root_int)
                printx('SHOWDOWN - ' + root_no_int + ' vs ' + root_int)
                if len(root_int) >= len(root_no_int) and len(root_int) > 0:
                    printx('ROOT WITH INTERFIX WINS')
                    return(basicResult2)
                    #self.root = [root_int]
                    pass
                else:
                    printx('ROOT WITHOUT INTERFIX WINS')
                    return(basicResult)
                            #self.root = [root_no_int]
                            #aself.interfix = []
            
        

        self.thirdResult = goThroughWord('')
        if len(self.firstResult.nopr.maxprefix) >0:
            printx(' -1 PREFIX')
            self.thirdResult = multiroot(self.firstResult.nopr.ostatok, PoS)
            if self.firstResult.nopr.maxprefix != None:
                self.thirdResult.extraPrefix = self.firstResult.nopr.maxprefix
        self.fourthResult = goThroughWord('')
        if len(self.secondResult.nopr.maxprefix) > 0:
            printx(' -2 PREFIX')
            self.fourthResult = multiroot(self.secondResult.nopr.ostatok, PoS)
            if self.secondResult.nopr.maxprefix != None:
               self.fourthResult.extraPrefix = self.firstResult.nopr.maxprefix
               self.fourthResult.extrasecond_prefix = self.secondResult.nopr.maxprefix
        self.fifthResult = goThroughWord('')
        printx('-0 PREFIX')
        self.fifthResult = multiroot(word, PoS)
        return
        
                            
    
class separator():
           

    def raspil(self, word):
        
        self.redflag = False
        self.reflexiveRemoved = False    # UBIRAEM REFLEXIVE

        word = word.lower()              # lOWERCASE
        self.originalWord = word
        if (word.endswith('ся') or word.endswith('сь'))&(len(word[:len(word)-2])>3):
            word = word[:len(word)-2]
            self.reflexiveRemoved = True
        analyz = mstm.analyze(word)
        if 'analysis' in analyz[0]:
            analyz = analyz[0]['analysis'][0]['gr']
        else:
            analyz = analyz[1]['analysis'][0]['gr']
        #analyz = mstm.analyze(word)[0]['analysis'][0]['gr']
        self.partofspeech = analyz.split(',')[0].split('=')[0]
        self.sklonenie_im_or_vin = False
        if self.partofspeech == 'S':    
            for z in analyz.split(','):
                if 'неод' in z or 'од' in z:
                    #print(z)
                    for x in ['им','вин']:
                        if x in z:
                            self.sklonenie_im_or_vin = True
                            break
                        else:
                            self.sklonenie_im_or_vin = False
                    
        else:
            self.sklonenie_im_or_vin = False
        for i in grStoplist:
            if analyz.startswith(i):
                self.redflag = True
                self.root = self.originalWord
                self.separated = self.originalWord
                printx('stopword, bailing out')
                return
        
        rslt = rootworks(word, self.partofspeech, self.sklonenie_im_or_vin)
        self.root = rslt.root
        self.prefix = rslt.prefix
        self.postfix = rslt.postfix
        self.suffix = rslt.suffix
        self.extraRoot = rslt.extraRoot
        self.interfix = rslt.interfix
        self.extraPrefix = rslt.extraPrefix
        self.extraSuffix = rslt.extraSuffix
        self.extrasecond_prefix = rslt.extrasecond_prefix
        self.morphList = []
        self.firstResult = rslt.firstResult
        self.secondResult = rslt.secondResult
        self.thirdResult = rslt.thirdResult
        self.fourthResult = rslt.fourthResult
        self.fifthResult = rslt.fifthResult
        self.morphList += self.extraRoot + self.interfix + self.prefix + self.root + self.suffix + self.postfix
        
        if self.reflexiveRemoved:
            self.reflexive =  self.originalWord[-2:]
            self.morphList += [self.reflexive]
            
        self.separated = ':'.join(self.morphList)
        self.enumerated = []
        
        for i,m in enumerate(self.morphList):
            self.enumerated.append((m,i))
    def assemble(self):
        self.morphList = []
        detachedSFX = ''
        detachedSFXlist = []
        sfxholder = []
        onemorecycle = True
        #printx('CYCLOOOOOOOOOO DADADADADADAM DA DA DAM - CCLO!')
        while onemorecycle:
            for sfx in suffixdict[self.partofspeech]:
                try:
                    if self.suffix[0][:len(self.suffix[0]) - len(detachedSFX)].endswith(sfx):
                        sfxholder.append(sfx)
                except:
                    #printx('too short!')
                    pass
            if len(sfxholder) > 0:
                detachedSFX = max(sfxholder, key = len) + detachedSFX
                detachedSFXlist = [max(sfxholder, key = len)] + detachedSFXlist
                sfxholder = []
            else:
                onemorecycle = False
        #printx(detachedSFXlist)
        self.suffix = detachedSFXlist #DANGEROUS FOR PROVERKAS
        
        self.morphList += self.extraPrefix + self.extraRoot + self.extraSuffix + self.interfix + self.second_prefix + self.prefix + self.root + self.suffix+ self.postfix
        
        if self.reflexiveRemoved:
            self.reflexive =  self.originalWord[-2:]
            self.morphList += [self.reflexive]
        if len(self.suffix) > 0:
            if self.partofspeech == 'V' and 'ал' == self.suffix[0]:
                self.suffix = ['a','л']
            
        self.separated = ':'.join([x for x in self.morphList if len(x)>0])
        self.enumerated = []
        
        for i,m in enumerate(self.morphList):
            self.enumerated.append((m,i))

    def __init__(self,word):
        self.raspil(word)
    
    
def get_winners(dict_of_competitors, modus):
        
    if modus == 'max':
        best_score = max(dict_of_competitors.values())
    elif modus == 'min':
        best_score = min(dict_of_competitors.values())
    else:
        raise ValueError('PROVIDE MODUS OF WINNER!')
    
    return[x for x in dict_of_competitors if dict_of_competitors[x] == best_score]
        
        
    
    
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
                #printx(pos)
                if (pos['status'] == 'корень' and pos['morph'] == root):
                    rootFound = True
#                    printx('NAWEL! ' + word)
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
                #printx(thing)
                #printx(unit)
                return(unit)
    def mat(self, morpheme):
        rootNum = self.matchPos(self.root[0])
        morphNum = self.matchPos(morpheme)
        #printx(self.root)
        #printx(morpheme)
        #printx(rootNum)
        #printx(morphNum)
        
        delta = rootNum[1] - morphNum[1]
        return([delta,rootNum,morphNum])
    def checkPos(self, morpheme,whatmorph = 'суффикс', bundle = None):
        if bundle == None:
            bundle = self.mat(morpheme)
#        printx(bundle)
        for word in self.wordlist:
            mPos = None
            rPos = None
            for pos in self.worddict[word]:
   #             printx(word)
                posNum = pos
                pos = self.worddict[word][pos]
                
                
                if (pos['morph'] ==  morpheme)&(pos['status'] == whatmorph) :
                    mPos = posNum
#                    printx('DABUDI')
                if pos['morph'] == self.root[0] :
#                    printx('DABUDAI')
                    rPos = posNum
            if (mPos != None and rPos != None):
                empDelta = int(rPos) - int(mPos)
#                printx(empDelta, rPos, mPos)
                if empDelta == bundle[0]:
                    printx('Yeach that is the word - ' + word)
                    return(True)
                    break
        printx('MORPHEME SHALL NOT PASS!')
        return(False)



class morphSplitnCheck(kuznecFinder, rootworks):
    
    
    
    
    def __init__(self,word):
        one_prefix = None
        two_prefix = None
        two_root_no_prefix = None
        #if globalCounter:
        #    for i in rootdict:
        #        if word in rootdict[i]:
        #            self.separated = word
        #            self.root = word
        #            self.originalWord = word
        #            return
        self.raspil(word)
        result_suffix_dict = {
                'first':0,
                'second':0,
                'fifth':0
                }
        result_root_dict = {
                'first':'',
                'second':'',
                'fifth':''
                }
        match_suffix_dict = {
                'first':'',
                'second':'',
                'fifth':''
                }
        scoreboard = {
                'first':0,
                'second':0,
                'fifth':0
                }
        if len(self.firstResult.suffix) > 0:
            result_suffix_dict.update({'first':len(self.firstResult.suffix[0])})
        if len(self.secondResult.suffix) > 0:
            result_suffix_dict.update({'second':len(self.secondResult.suffix[0])})
        if len(self.fifthResult.suffix) > 0:
            result_suffix_dict.update({'fifth':len(self.fifthResult.suffix[0])})
        #if len(self.firstResult.root[0]) > 0:
        #    result_root_list.append(self.firstResult.root)
        if len(self.firstResult.root) > 0:
            result_root_dict['first'] = self.firstResult.root[0]
        
        if len(self.secondResult.root) > 0:
            result_root_dict['second'] = self.secondResult.root[0]
        if len(self.fifthResult.root) > 0:
            result_root_dict['fifth']= self.fifthResult.root[0]
        
        
      # {'first':len(self.firstResult.suffix[0]),'second':len(self.secondResult.suffix),'fifth':len(self.fifthResult.suffix)}
        if self.redflag == True:
            return
#        self.grab(self.firstResult)
#        self.assemble()
        
        try:
            if len(self.suffix) > 0:
                if len(self.suffix[0]) >0 :                        
                    #one_prefix = self.do_check(self.suffix[0])
                    cycle_cash = self.cycleThroughMorph(self.suffix)
                    one_prefix = cycle_cash[0]
                    if one_prefix:
                        print('ONE PREFIX IS HERE')
                        match_suffix_dict['first']=cycle_cash[1]
        except:
            pass
        self.grab(self.secondResult)
        self.assemble()
        try:
            if len(self.suffix) > 0:        
                #two_prefix = self.do_check(self.suffix[0])
                cycle_cash = self.cycleThroughMorph(self.suffix)
                two_prefix = cycle_cash[0]
                if two_prefix:
                    print('TWO PREFIX IS HERE')
                    match_suffix_dict['second']=cycle_cash[1]
                    #scoreboard['second'] += 1
        except:
            pass

        self.grab(self.fifthResult)
        self.assemble()
#
        if len(self.fifthResult.suffix) > 0:
            if len(self.fifthResult.suffix[0]) > 0:
                try:
                    self.grab(self.fifthResult)
                    self.assemble()
                    cycle_cash = self.cycleThroughMorph(self.suffix)
                    two_root_no_prefix = cycle_cash[0]
                    if two_root_no_prefix:
                        print('THREE PREFIX IS HERE')
                        match_suffix_dict['fifth']=cycle_cash[1]
                        #scoreboard['fifth'] += 1
#                        printx('MULTIPREFIX WINS')
#                        return
                except:
                    pass
                
        
#            if not two_root_no_prefix: #TUT DORABOTAT'!!
#                printx(self.root,self.suffix)
#                if len(self.root)>0:
#                    if (len(self.root[0]) > 2)&(len(self.suffix)==0):
#                        printx('MULTIPREFIX DEEMED WORTHY')
#                        return
        #if len(result_suffix_dict) > 0:
       #     chosen_one = m(result_suffix_dict.items(), key=operator.itemgetter(1))[0]
       #     scoreboard[chosen_one]+= 1
        morphListLength = {}
        rootLength = {}
        self.grab(self.firstResult)
        self.assemble()
        print(self.separated)
        try:
            rootLength['first']=len(self.root[0])
            morphListLength['first']=len([x for x in self.morphList if len(x)>0])
        except:
            pass
        self.grab(self.secondResult)
        self.assemble()
        print(self.separated)
        try:
            rootLength['second']=len(self.root[0])
            morphListLength['second']=len([x for x in self.morphList if len(x)>0])
        except:
            pass
        self.grab(self.fifthResult)
        self.assemble()
        print(self.separated)
        try:
            rootLength['fifth']=len(self.root[0])
            morphListLength['fifth']=len([x for x in self.morphList if len(x)>0])
        except:
            pass
        if self.partofspeech == 'S':
            print('result_suffix_dict',result_suffix_dict)
            for x in get_winners(result_suffix_dict,'min'):
                scoreboard[x] += 1
                if (result_suffix_dict[x] == 0)&(len(result_root_dict[x])>2):
                    scoreboard[x] += 1
      
        print('morphListLength', morphListLength)

        for x in get_winners(morphListLength,'min'):
            
            scoreboard[x]+= 1
        print('rootLength',rootLength)
   
        for x in get_winners(rootLength,'max'):
            
            scoreboard[x]+= 1
        print('match_suffix_dict',match_suffix_dict)
        for x in get_winners(match_suffix_dict,'max'):
            scoreboard[x]+= 1
        winner = max(scoreboard.items(), key=operator.itemgetter(1))[0]
        
        print('scoreboard', scoreboard) 
        print(winner)
       
        
        
        if winner == 'first':
            self.grab(self.firstResult)
            self.assemble()
            self.morphList = []
            self.morphList += self.extraPrefix + self.extraRoot + self.extraSuffix + self.interfix + self.second_prefix + self.prefix + self.root + self.suffix+ self.postfix
        
            if self.reflexiveRemoved:
                self.reflexive =  self.originalWord[-2:]
                self.morphList += [self.reflexive]
        
            
            self.separated = ':'.join([x for x in self.morphList if len(x)>0])

            if len(self.separated) > len(self.originalWord):
                return
            else:
                winner = 'second'
        if winner == 'second':
            self.grab(self.secondResult)
            self.assemble()
            self.morphList = []
            self.morphList += self.extraPrefix + self.extraRoot + self.extraSuffix + self.interfix + self.second_prefix + self.prefix + self.root + self.suffix+ self.postfix
        
            if self.reflexiveRemoved:
                self.reflexive =  self.originalWord[-2:]
                self.morphList += [self.reflexive]
        
            
            self.separated = ':'.join([x for x in self.morphList if len(x)>0])

            if len(self.separated) > len(self.originalWord):
                return
            else:
                winner = 'fifth'
        if winner == 'fifth':
            self.grab(self.fifthResult)
            self.assemble()
            self.morphList = []
            self.morphList += self.extraPrefix + self.extraRoot + self.extraSuffix + self.interfix + self.second_prefix + self.prefix + self.root + self.suffix+ self.postfix
        
            if self.reflexiveRemoved:
                self.reflexive =  self.originalWord[-2:]
                self.morphList += [self.reflexive]
        
            
            self.separated = ':'.join([x for x in self.morphList if len(x)>0])

            if len(self.separated) > len(self.originalWord):
                return
        #print(scoreboard)
        #print(max(scoreboard.items(), key=operator.itemgetter(1))[0])
        
        
        
        
#        else:
#                if (len(self.secondResult.root[0]) > len(self.fifthResult.root[0]) + 1)&(len(self.fifthResult.root[0]) < 3):
#                    printx('ljhujkbmada')
#                    self.grab(self.firstResult)
#                    self.assemble()
                    
        '''
        try:
            if len(self.suffix) > 0:
                if len(self.suffix[0]) >0 :                        
                    one_prefix = self.do_check(self.suffix[0])
        except:
            pass
        self.grab(self.secondResult)
        self.assemble()
        try:
            if len(self.suffix) > 0:        
                two_prefix = self.do_check(self.suffix[0])
        except:
            pass
        self.grab(self.firstResult)
        self.assemble()
        if (one_prefix == True)&(len(self.suffix) <3):
            printx()
            self.grab(self.firstResult)
            self.assemble()
            printx('odna pristavka')
        elif (two_prefix == True)&(len(self.suffix) <3):                                # IF SUCCESS FOR FIRSTRESULT SUFFIX
            self.grab(self.secondResult)
            self.assemble()
            printx('dva pristaka')
#        elif (one_prefix == None):
#            self.grab(self.firstResult)
#            self.assemble()
#            printx('maybe one')
#        elif two_prefix == None:
#            self.grab(self.secondResult)
#            self.assemble()
#            printx('maybe two')
        else:                               # MULTIROOT SHAKES IN

            if (len(self.firstResult.root) > 0)&(len(self.fifthResult.root) > 0):
                if (len(self.firstResult.root[0]) > len(self.fifthResult.root[0]) + 1)&(len(self.fifthResult.root[0]) < 4):
                    printx('ljhujkbmada')
                    self.grab(self.firstResult)
                    self.assemble()
                    return
            self.grab(self.fifthResult)
            self.assemble()
            #printx('nihuja')
            if len(self.fifthResult.suffix) > 0:
                if len(self.fifthResult.suffix[0]) > 0:
                    self.grab(self.fifthResult)
                    self.assemble()
                    #self.sfxcash = []
                    #two_root_no_prefix = Nonew
                    #for i in stmr.gtsfx():
    #        printx(i)
                    #    if self.suffix[0].startswith(i):
                    #        self.sfxcash.append(i)
                            #self.sfxdict[i] = [i]
                    #for i in Carthes(self.rootdict['суффикс'],self.rootdict['суффикс']):
                    #    if max(self.sfxcash, key = len) in i: # PROBABLY TUT POMENJAT'!!!!!!!!!!!!1 NA FULL SUFFIX
                    #        two_root_no_prefix = True
                            #printx(two_root_no_prefix)
                            #printx(i, max(self.sfxcash, key = len))
                    two_root_no_prefix = self.cycleThroughMorph(self.suffix)
                    if two_root_no_prefix:
                        printx('MULTIPREFIX WINS')
                        return
            if not two_root_no_prefix: #TUT DORABOTAT'!!
                printx(self.root,self.suffix)
                if len(self.root)>0:
                    if (len(self.root[0]) > 2)&(len(self.suffix)==0):
                        printx('MULTIPREFIX DEEMED WORTHY')
                        return
                if len(result_suffix_dict) > 0:
                    chosen_one = min(result_suffix_dict.items(), key=operator.itemgetter(1))[0]
                    if chosen_one == 'first':
                        printx('V SOSTYAZANII SUFFIXOV POBEDIL FIRSTRESULT')
                        self.grab(self.firstResult)
                        self.assemble()
                        return
                    elif chosen_one == 'second':
                        printx('V SOSTYAZANII SUFFIXOV POBEDIL SECONDRESULT')
                        self.grab(self.secondResult)
                        self.assemble()
                        return
                    elif chosen_one == 'fifth':
                        printx('V SOSTYAZANII SUFFIXOV POBEDIL FIFTHRESULT')
                        return
                printx('labmada')
                self.grab(self.firstResult)
                self.assemble()
            else:
                if (len(self.secondResult.root[0]) > len(self.fifthResult.root[0]) + 1)&(len(self.fifthResult.root[0]) < 3):
                    printx('ljhujkbmada')
                    self.grab(self.firstResult)
                    self.assemble()
                    
            '''
    def cycleThroughMorph(self, morpheme):
        concatenated = ''.join(morpheme)
        for i in range(len(concatenated)):
            inner_suffix = concatenated[:i+1]
            self.notinit(self.root)
            inner_flag = self.checkPos(inner_suffix,bundle = [-1] )
            if inner_flag == True:
                print('DA, TRUE! suffix:', inner_suffix)
                return([True,inner_suffix])
        return([False,''])
            

        
    def do_check(self,morph, whatmorph = 'суффикс'):
        
        self.notinit(self.root)
        flag = self.checkPos(morph, whatmorph)
        if flag:
            return True
        else: 
            return False
globalCounter = 0
zzjay = morphSplitnCheck('лоб')
globalCounter += 1


def goThroughCorpus(inp, outputPath):
    inpts = open('\\resources\\'+inp,'r',encoding = 'utf-8')
    outputPath = '\\resources\\'+inp+'\\' + outputPath
    csvCash = 'Original\tSeparated\n'
    for item in inpts:
        item = item.replace('\n','')
        printx(item)
        t = morphSplitnCheck(item)
#        t.grab(t.fifthResult)
#        t.assemble()
        csvCash += t.originalWord + '\t' + t.separated.replace('::',':') + '\n'
        #csvCash += t.originalWord + '\t' + ':'.join([t.fifthResult.extraRoot[0],t.fifthResult.prefix[0],t.fifthResult.root[0],t.fifthResult.suffix[0],t.postfix[0]])+ '\n'
    dumpling = open(outputPath, 'w', encoding = 'utf-8')
    dumpling.write(csvCash)
    dumpling.close()

pass
    


