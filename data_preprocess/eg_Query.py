# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

#import nltk
#from nltk import word_tokenize
#from nltk.corpus import stopwords
import re
import nltk.stem

import nltk
from nltk.corpus import stopwords

from mySql import QuerymySql


print("loading......")
read=[]
s = nltk.stem.SnowballStemmer('english')
read1=QuerymySql("localhost", "root","123456","recall","utf8","select distinct 制造商 from Recall")
stop_words = set(stopwords.words("english"))
for w in ['!',',','.','?','-s','-ly','</s>','s','(',')','due']:
    stop_words.add(w)

for name in read1:
    name = re.findall("\(\'(.*?)\',\)", str(name))[0]
    with open("datas/recall_"+name+".train", "w", encoding='utf-8') as f:
        read2 = QuerymySql("localhost", "root", "123456", "recall", "utf8",
                           "select 缺陷情况 from (select * from Recall GROUP BY `制造商`,`召回时间` HAVING Count(*)>=1) AS a where `制造商` ='"+str(name)+"'")
        for element in read2:
            try:
                words = re.findall("\(\'(.*?)\',\)", str(element))[0]
            except:
                words = re.findall("\(\"(.*?)\",\)", str(element))[0]
            words=nltk.word_tokenize(words.lower())
            filtered_sentence = [w for w in words if not w in stop_words]
            for word in filtered_sentence:
               word=s.stem(word)
               f.write(word+" ")
            f.write("\r\n")
print("end")
