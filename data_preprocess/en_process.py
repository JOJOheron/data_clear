import nltk.stem
from nltk.corpus import stopwords

"""
a class to preprocess english sentences——remove stopwords(add extral stopwords)、
change to lowercase、seperate sentences
it returns a string
"""

def en_preprocess(text,add_stopwords=None):
  output=""
  s = nltk.stem.SnowballStemmer('english')
  stop_words = set(stopwords.words("english"))
  text= nltk.word_tokenize(text.lower())
  try:
      for w in add_stopwords:
          stop_words.add(w)
  except:
      pass
  filtered_sentence = [w for w in text if not w in stop_words]
  for word in filtered_sentence:
      word=s.stem(word)
      output+=word
      output+=" "
  return output
