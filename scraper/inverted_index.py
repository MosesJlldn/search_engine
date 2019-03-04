import os
import csv
import re

def sorted_aphanumeric(data):

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

all_docs_dict = []

path = 'C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\lemmatization\\lemmatized_texts' #path to html_texts

words_in_docs = []
listdir = os.listdir(path)
sorted_listdir = sorted_aphanumeric(listdir)

for lemm_text in sorted_listdir:

	with open(path + '\\' + lemm_text, 'r') as f:

		reader = csv.reader(f)
		data = []
		data = [row for row in reader]
		words_in_doc = data[0]
		words_in_docs.append(words_in_doc)
		not_in_all_dict = [word for word in words_in_doc if word not in all_docs_dict]
		all_docs_dict.extend(not_in_all_dict)

dict_size = len(all_docs_dict)

words_indicies = []

for index, words in enumerate(words_in_docs):

	word_indicies = []

	for dict_word in all_docs_dict:

		if (dict_word in words):

			word_indicies.append(index)

	words_indicies.append(word_indicies)

print(words_indicies)