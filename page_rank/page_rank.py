import csv, operator
from collections import OrderedDict

# !!! ATTENTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# На сайте matprofi из-за боковой панели (навигатора по сайту) все ссылки ссылаются на все, ПОЭТОМУ учитывались только ссылки находившиеся внутри статьи, а не всей страницы.
# По этой же причине главная страница не меняет свой рейтинг.

def read_links():

	with open('links_map.csv', 'r', newline='') as f:

		reader = csv.reader(f)
		data = [row for row in reader] 
		keys = [row[0] for row in data]
		values = [row[1:] for row in data]

		return dict(zip(keys, values))

def calc_page_rank(page, links_map, page_rank_map, links_on_page_map, N, d=0.75):

	connected_links = [key for key, value in links_map.items() if page in value] #links that refer to page

	sum_list = [(page_rank_map[link] / links_on_page_map[link]) for link in connected_links]
	res = ((1 - d) / N) + sum(sum_list)

	return res

if __name__=="__main__":

	links_map = read_links() # key - page, value - links on page
	links = list(links_map.keys()) # all page links names

	links_amount = [len(value) for key, value in links_map.items()]
	links_on_page_map = dict(zip(links, links_amount))

	N = len(links_map)
	page_rank = [1 / N for i in range(0, 100)]
	page_rank_map = dict(zip(links, page_rank))
	
	for i in range(0, 50):
		page_rank = []
		page_rank = [calc_page_rank(page, links_map, page_rank_map, links_on_page_map, N) for page in links]
		page_rank_map = dict(zip(links, page_rank))

	sorted_result = sorted(page_rank_map.items(), key=operator.itemgetter(1), reverse=True)

	with open('result.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(sorted_result)

	print(sorted(page_rank_map.items(), key=operator.itemgetter(1), reverse=True))
