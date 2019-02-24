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
from collections import Counter

def lemmatize_text(text):

	# tokenizer = RegexpTokenizer(r'\w+')
	# words = tokenizer.tokenize(text.lower())

	lemmatizer = Mystem() 
	lemmatized_words = lemmatizer.lemmatize(text) # [lemmatizer.lemmatize(f) for f in filtered_words]
	stop_words = stopwords.words("russian")
	stop_words.extend(['...', '«', '»', '–'])
	filtered_words = [w for w in lemmatized_words if w not in stop_words and w != " " and w.strip() not in punctuation]

	return filtered_words

for html_text_file in os.listdir('scraper/webpage_text'):
	with open('webpage_text/' + html_text_file, 'r') as myfile:
		text=myfile.read().replace('\n', ' ')
		text = re.sub(' +', ' ', text)
		lemmatized_text = lemmatize_text(text)
		words_count = Counter(lemmatized_text)
		with open('lemmatized_texts/' + html_text_file + '_lemmatized.csv', 'w', newline='') as f:
			w = csv.DictWriter(f, words_count.keys())
			w.writeheader()
			w.writerow(words_count)
