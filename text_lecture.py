# text lectures 

#%% 
import nltk
from nltk.corpus import stopwords

word_list = ["this","is", "an","example"]
filtered_words = [w for w in word_list if not w in stopwords.words('english')]
print filtered_words

# stemming
#%%
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("germany")


# TfIdf term frequency onverse document frequency

