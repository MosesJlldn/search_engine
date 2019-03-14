import ast, csv
from pymystem3 import Mystem

bool_op = ['NOT', 'AND', 'OR']
bool_op_code = [-1, -2, -3]

with open('C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\inverted_index\\inverted_index.csv', 'r', newline='') as f:

	reader = csv.reader(f)
	data = [row for row in reader]
	words = data[0]
	inverted_indicies = data[1]

request = "вынести AND Всевозможный AND минус"

lemmatizer = Mystem() 
lemmatized_request = lemmatizer.lemmatize(request)
lemmatized_request = [w for w in lemmatized_request if w not in [" ", "\n"]]

for index, item in enumerate(lemmatized_request):

	if (item in bool_op): 

		lemmatized_request[index] = [bool_op_code[bool_op.index(item)]]

	if (item not in bool_op):

		lemmatized_request[index] = ast.literal_eval(inverted_indicies[words.index(item)])

def and_operation():

	left = 0
	right = 0

	for index, item in enumerate(lemmatized_request):

		res = []

		if (item == [-2]):
			print('entering')
			left = index - 1
			right = index + 1

			if (lemmatized_request[right] == [-3]):

				right += 1
				res = [i for i in lemmatized_request[left] if i not in lemmatized_request[right]]
			else:

				lemmatized_request[left].extend(lemmatized_request[right])

			new_lemmatized_request = [i for rindex, i in enumerate(lemmatized_request) if rindex < index]
			new_lemmatized_request.extend([i for rindex, i in enumerate(lemmatized_request) if rindex > right])
			lemmatized_request = new_lemmatized_request
			print(lemmatized_request)
			print('end\n')
			and_operation(lemmatized_request)
			break

	print("check")
	print(lemmatized_request)
	return lemmatized_request

print(lemmatized_request)
print('\n')
res = and_operation(lemmatized_request)

