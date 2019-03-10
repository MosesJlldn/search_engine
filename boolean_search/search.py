import ast, csv
from pymystem3 import Mystem

bool_op = ['NOT', 'AND', 'OR']
bool_op_code = [-1, -2, -3]

def and_operation(request):

	left = 0
	right = 0

	for index, item in enumerate(request):

		print("check")
		print(request)

		res = []

		if (item == [-2]):
			print('entering')
			left = index - 1
			right = index + 1

			if (request[right] == [-3]):

				right += 1
				res = [i for i in request[left] if i not in request[right]]
			else:

				request[left].extend(request[right])

			new_request = [i for rindex, i in enumerate(request) if rindex < index]
			new_request.extend([i for rindex, i in enumerate(request) if rindex > right])
			request = new_request
			print(request)
			print('end\n')
			and_operation(request)
			break

	return request

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

print(lemmatized_request)
print('\n')
res = and_operation(lemmatized_request)


