import ast, csv, os, re, webbrowser, sys
from nltk.tokenize import word_tokenize
from pymystem3 import Mystem

def intersection(lst1, lst2): 

    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

with open('C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\inverted_index\\inverted_index.csv', 'r', newline='') as f:

	reader = csv.reader(f)
	data = [row for row in reader]
	words = data[0]
	inverted_indicies = data[1]

request = "вынести Всевозможный минус ыдлвоардлывор"
#request = sys.argv[1]	

lemmatizer = Mystem() 
lemmatized_request = lemmatizer.lemmatize(request)
lemmatized_request = [w for w in lemmatized_request if w not in [" ", "\n"]]

doc_sets = []

for index, item in enumerate(lemmatized_request):

	try:

		doc_sets.append(ast.literal_eval(inverted_indicies[words.index(item)]))
	except ValueError:

		pass

sets_intersection = []

for index, item in enumerate(doc_sets):

	if (index == 0):

		sets_intersection = item
	else:

		sets_intersection = intersection(sets_intersection, item)

path = 'C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\scraper\\URLs_list.txt'
main_page = 'http://mathprofi.ru/'

with open(path) as f:

    content = f.readlines()
    content = [x.strip() for x in content]

for i in sets_intersection:

    page = word_tokenize(content[i])[1]
    url = main_page + page
    #webbrowser.open(url,new=2)
    print(url)