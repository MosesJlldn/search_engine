import ast, math, csv
from pymystem3 import Mystem

with open('C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\tf_idf\\td_idf.csv', 'r', newline='') as f:

	reader = csv.reader(f)
	data = [row for row in reader]
	words = data[0]
	tf_idfs = data[1]

with open('C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\tf_idf\\idfs.csv', 'r', newline='') as f:

	reader = csv.reader(f)
	data = [row for row in reader]
	words = data[0]
	idfs = data[1]

tf_idfs = [ast.literal_eval(list) for list in tf_idfs]
idfs = [ast.literal_eval(list) for list in idfs]

request = "вынести Всевозможный минус ыдлвоардлывор"
lemmatizer = Mystem() 
lemmatized_request = lemmatizer.lemmatize(request)
lemmatized_request = [w for w in lemmatized_request if w not in [" ", "\n"]]

docs_vectors_length = []

doc_count = 100
words_count = len(words)

for doc_index in range(0, doc_count):

	current_doc_length = 0

	for word_index in range(0, words_count):

		current_doc_length += tf_idfs[word_index][doc_index] * tf_idfs[word_index][doc_index] # to the second degree

	current_doc_length = math.sqrt(current_doc_length)

	docs_vectors_length.append(current_doc_length)

