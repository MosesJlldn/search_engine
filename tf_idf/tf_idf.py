import os
import csv
import re
from math import log
from collections import Counter

def sorted_aphanumeric(data):

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

path = 'C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\lemmatization\\lemmatized_texts' #path to lemmatized_texts

docs = []
listdir = os.listdir(path)
sorted_listdir = sorted_aphanumeric(listdir)

all_docs_dict = []

for lemm_text in sorted_listdir:

	with open(path + '\\' + lemm_text, 'r') as f:

		reader = csv.reader(f)
		data = []
		data = [row for row in reader]
		words_in_doc = data[0]
		docs.append(words_in_doc)
		not_in_all_dict = [word for word in words_in_doc if word not in all_docs_dict]
		all_docs_dict.extend(not_in_all_dict)

tfs_for_all_words = [] # occurences per document
idfs_for_all_words = [] # documents containing term 
TFIDF_for_all_words = [] # word ratings per document
total_number_of_doc = len(docs)

for index, word in enumerate(all_docs_dict):

	tf_for_one_word = []
	idf_for_one_word = 0

	for index, doc in enumerate(docs):

		tf_for_one_word_in_current_doc = 0
		is_word_occured_in_current_doc = False

		for index, occurence in enumerate(doc):

			if (occurence == word):

				tf_for_one_word_in_current_doc += 1
				is_word_occured_in_current_doc = True

		tf_for_one_word.append(tf_for_one_word_in_current_doc / len(docs))

		if (is_word_occured_in_current_doc):

			idf_for_one_word += 1

	tfs_for_all_words.append(tf_for_one_word)
	idfs_for_all_words.append(idf_for_one_word)

#make idf real idf
idfs_for_all_words = [log(total_number_of_doc / word) for word in idfs_for_all_words]

for windex, word in enumerate(all_docs_dict):

	TFIDF_for_one_word = []

	for dindex, doc in enumerate(docs):

		TFIDF_for_one_word_in_current_doc = tfs_for_all_words[windex][dindex] * idfs_for_all_words[windex]
		TFIDF_for_one_word.append(TFIDF_for_one_word_in_current_doc)

	TFIDF_for_all_words.append(TFIDF_for_one_word)

result = dict(zip(all_docs_dict, TFIDF_for_all_words))

idfs_result = dict(zip(all_docs_dict, idfs_for_all_words))
tfs_result = dict(zip(all_docs_dict, tfs_for_all_words))

with open('idfs.csv', 'w', newline='') as f:

	w = csv.DictWriter(f, idfs_result.keys())
	w.writeheader()
	w.writerow(idfs_result)

with open('tfs.csv', 'w', newline='') as f:

	w = csv.DictWriter(f, tfs_result.keys())
	w.writeheader()
	w.writerow(tfs_result)

with open('td_idf.csv', 'w', newline='') as f:
	
	w = csv.DictWriter(f, result.keys())
	w.writeheader()
	w.writerow(result)