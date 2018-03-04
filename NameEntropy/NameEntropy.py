
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sc
#import sklearn
import sys
import types
import codecs
import re
import string
import csv
import codecs
#import nltk


# check number in domain
def number(domain):
    length = len(domain)
    rate = 0
    index = domain.find("0")
    rate = index/length
    if rate < 0 :
        rate = 0
    return rate

def containNum(domain):
    n = domain.count("0")
    if n > 0 :
        n = 1
    return n 


# Count each unigram
def unigram(text):
    uni = []
    uniNum = 0
    while uniNum < 3 :
        uni.append(0)
        uniNum += 1
    AllUni = ['0','1','2']
    u = 0
    uniSum = 0
    while u < len(AllUni) :
         uniSum += text.count(AllUni[u])
         u += 1
    u = 0
    while u < len(AllUni) :
         #print(text.count(AllUni[u]))
         uni[u] = text.count(AllUni[u])/uniSum
         u += 1
    #print(uniSum)
    #print(uni)
    return uni

# Count each bigram
def bigram(text):
    bi = []
    biNum = 0
    while biNum < 9 :
        bi.append(0)
        biNum += 1
    AllBi = ["00","01","02",\
             "10","11","12",\
             "20","21","22"]
    b = 0
    biSum = 0
    while b < len(AllBi) :
         biSum += text.count(AllBi[b])
         b += 1
    b = 0
    while b < len(AllBi) :
         bi[b] = text.count(AllBi[b])/biSum
         b += 1
    #print(bi)
    return bi

# Count each trigram
def trigram(text):
    tri = []
    triNum = 0
    while triNum < 27 :
        tri.append(0)
        triNum += 1
    AllTri = ["000","001","002",\
              "010","011","012",\
              "020","021","022",\
              "100","101","102",\
              "110","111","112",\
              "120","121","122",\
              "200","201","202",\
              "210","211","212",\
              "220","221","222"]
    t = 0
    triSum = 0
    while t < len(AllTri) :
         triSum += text.count(AllTri[t])
         t += 1
    t = 0
    while t < len(AllTri) :
         tri[t] = text.count(AllTri[t])/triSum
         t += 1
    #print(tri)
    return tri

# Calculate Entropy
def Entropy(p):
    p = np.ma.array(p)
    return -(p * np.ma.log(p)).sum()

# CSVファイル作成
openCSV = open('DomainNameEntropy.csv', 'w')
writecsv = csv.writer(openCSV, lineterminator ='\n')
rowHeader = (("JsName","1g_entropy","2g_entopy","3g_entropy", "index","containNum"))
writecsv.writerow(rowHeader)
row = []

csvfile = open("name.csv")
for url in csv.reader(csvfile):
    print(url[0])  

    toNum = re.sub(r'[0-9]', '0', url[0])
    toEng = re.sub(r'[a-z]', '1', toNum)
    toEtc = re.sub(r'[^0-9a-z]', '2', toEng)
    print(toEtc)
    
    uniEnt = Entropy(unigram(toEtc))
    biEnt = Entropy(bigram(toEtc))
    triEnt = Entropy(trigram(toEtc))
    checkNum = number(toEtc)  

    print(uniEnt)
    print(biEnt)
    print(triEnt)  
    print(checkNum)
    print(containNum(toEtc))  
    
    print("")

    row.append((url[0], uniEnt, biEnt, triEnt, checkNum, containNum(toEtc)))   

writecsv.writerows(row)
openCSV.close 
