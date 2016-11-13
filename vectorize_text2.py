#!/usr/bin/python

import os
import pickle
import re
import sys
from parse_out_email_text import parseOutText
from sklearn.feature_extraction.text import TfidfVectorizer


sys.path.append("../ud120-projects/tools/")

"""
part 2
expect part 1 wo the 2 at the end
"""


word_data = pickle.load(open("your_word_data.pkl", "r"))
from_data = pickle.load(open("your_email_authors.pkl", "r"))


# ## in Part 4, do TfIdf vectorization here

print word_data[152]

tfidf_vector = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf_vector.fit_transform(word_data, from_data)


feature_names = tfidf_vector.get_feature_names()
print len(feature_names)

print feature_names[34597]
