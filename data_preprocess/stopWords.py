def stopwords(segs):
    with open("stop.txt", "r", encoding='utf-8') as r:
        stopwordslist = r.readlines()
        slist=[]
        for stopwords in stopwordslist:
            stopwords=stopwords.split("\n")[0]
            slist.append(stopwords)
    final = ""
    segs = segs.split(" ")
    for seg in segs:
        if seg not in slist:
           final+=seg
           final+=" "
    return(final)