import ast, csv
from pymystem3 import Mystem

def sorted_aphanumeric(data):

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def read_data():

	words = []
	tfs = []
	idfs = []

	with open('C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\tf_idf\\tfs.csv', 'r', newline='') as f:

		reader = csv.reader(f)
		data = [row for row in reader]
		words = data[0]
		tfs = data[1]
		tfs = [ast.literal_eval(lst) for lst in tfs]

	with open('C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\tf_idf\\idfs.csv', 'r', newline='') as f:

		reader = csv.reader(f)
		data = [row for row in reader]
		idfs = data[1]

	return [words, tfs, idfs]

def read_doc_length():

	path = 'C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\lemmatization\\lemmatized_texts\\'
	listdir = os.listdir(path)
	sorted_listdir = sorted_aphanumeric(listdir)

	docs_length = []

	for lemm_text in sorted_listdir:

		with open(path + '\\' + lemm_text, 'r') as f:

			reader = csv.reader(f)
			data = [row for row in reader]
			words = data[0]
			count = data[1]
			docs_length.append(sum(count))

	return docs_length

def score(idf, tf, d, avgdl, k=2.0, b=0.75):

	res = (idf * tf * (k + 1)) / (tf + k * (1 - b + b * d / avgdl))

	return res

def preprocess_query(query):

	lemmatizer = Mystem() 
	lemmatized_query = lemmatizer.lemmatize(query)
	lemmatized_query = [w for w in lemmatized_query if w not in [" ", "\n"]]

	return lemmatized_query

if __name__ == "__main__":

	docs_length = read_doc_length()
	avgdl = sum(docs_length) / len(docs_length)

	query = "как считать интегралы"
	preprocessed_query = preprocess_query(query)

	docs_score = []

	for i in range (0, 99):

		docs_score.append(score())