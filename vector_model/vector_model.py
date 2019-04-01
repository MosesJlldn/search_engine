import ast, math, csv, numpy, operator
from pymystem3 import Mystem
from nltk.tokenize import word_tokenize

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

tf_idfs = [ast.literal_eval(lst) for lst in tf_idfs]
idfs = [ast.literal_eval(lst) for lst in idfs] 

request = 'интеграл первого порядка' #"вынести Всевозможный минус ыдлвоардлывор"
lemmatizer = Mystem() 
lemmatized_request = lemmatizer.lemmatize(request)
lemmatized_request = [w for w in lemmatized_request if w not in [" ", "\n"]]

docs_vectors_length = []
docs_vectors = []

doc_count = 100
words_count = len(words)

for doc_index in range(0, doc_count):

	current_doc_length = 0
	current_vector = []

	for word_index in range(0, words_count):

		current_doc_length += tf_idfs[word_index][doc_index] * tf_idfs[word_index][doc_index] # to the second degree
		current_vector.append(tf_idfs[word_index][doc_index])

	current_doc_length = math.sqrt(current_doc_length)

	docs_vectors.append(current_vector)
	docs_vectors_length.append(current_doc_length)

#doc_vectors_calculated

query_vector_length = 0
query_vector = []
	
for index, word in enumerate(words):

	query_vector.append(0)

	for req_word in lemmatized_request:

		if (req_word == word):

			query_vector[index] += 1

	if (query_vector[index] != 0):

		query_vector[index] /= len(lemmatized_request)
		query_vector[index] *= idfs[index]

for word in lemmatized_request:

	try:
		query_vector_length += idfs[words.index(word)] * idfs[words.index(word)]  # to the second degree
	except ValueError:

		pass

query_vector_length = math.sqrt(query_vector_length)

#query vector calculated
# A = query_vector, B = docs_vectors[i], ||A|| = query_vector_length, ||B|| = docs_vectors_length[i]

query_vector = numpy.array(query_vector)
docs_vectors = numpy.array(docs_vectors)

vector_mult = docs_vectors.dot(query_vector)
vector_length_mult = [dvl * query_vector_length for dvl in docs_vectors_length]

similarity = vector_mult / vector_length_mult

path = 'C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\scraper\\URLs_list.txt'
main_page = 'http://mathprofi.ru/'

with open(path) as f:

    content = f.readlines()
    content = [x.strip() for x in content]

result = dict(zip(content, similarity))

print(sorted(result.items(), key=operator.itemgetter(1), reverse=True))