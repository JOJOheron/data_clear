import jieba
from stopWords import stopwords

def seg(string):
    text = jieba.cut(string)  # 进行分词
    text = ' '.join(text)
    text = stopwords(text)
    return text