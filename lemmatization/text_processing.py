from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from pymystem3 import Mystem
import numpy as np
from string import punctuation
import os
import csv
import re
import string
from collections import Counter

def lemmatize_text(text):

	lemmatizer = Mystem() 
	lemmatized_words = lemmatizer.lemmatize(text)
	stop_words = stopwords.words("russian")
	stop_words.append('…')
	filtered_words = [w for w in lemmatized_words if w not in stop_words and w != " " and w.strip() not in punctuation]

	return filtered_words

path = '' #path to html_texts

for html_text_file in os.listdir(path):

	with open(path + '\\' + html_text_file, 'r') as myfile:

		text = myfile.read().replace('\n', ' ')
		text = re.sub(' +', ' ', text)
		exclude = string.punctuation + '–«»'
		text = ''.join(ch for ch in text if ch not in exclude)
		lemmatized_text = lemmatize_text(text)
		words_count = Counter(lemmatized_text)

		with open('lemmatized_texts/' + html_text_file + '_lemmatized.csv', 'w', newline='') as f:
			
			w = csv.DictWriter(f, words_count.keys())
			w.writeheader()
			w.writerow(words_count)
