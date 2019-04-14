import csv

def read_links():

	with open('links_map.csv', 'r', newline='') as f:

		reader = csv.reader(f)
		values = [row[1:] for row in reader]
		print(values)
		keys = [row[:1] for row in reader]

		
		return dict(zip(keys, values))

if __name__=="__main__":

	links_map = read_links()
	print (links_map)
