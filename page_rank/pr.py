import csv

def read_links():

	with open('links_map.csv', 'r', newline='') as f:

		reader = csv.reader(f)
		data = [row for row in reader] 
		keys = [row[0] for row in data]
		values = [row[1:] for row in data]

		return dict(zip(keys, values))

def calc_page_rank(page, links_map, N, d=0.75):

	connected_links = [key for key, value in links_map.items() if page in value]
	return connected_links

if __name__=="__main__":

	links_map = read_links()
	links = list(links_map.keys())
	N = len(links_map)
	page_rank = [1 / N for i in range(0, 100)]
	print(links[1])
	print(calc_page_rank(links[1], links_map, N))