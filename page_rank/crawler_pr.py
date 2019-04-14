import scrapy
import csv
from nltk.tokenize import word_tokenize

class MathprofiSpider(scrapy.Spider):
	name = "mathprofi_spider"
	start_urls = ['http://mathprofi.ru/']
	main_page = 'http://mathprofi.ru/'
	current_page = 'http://mathprofi.ru/'
	page_count = 1

	def parse(self, response):

		links = []
		links.append(self.current_page)

		MAIN_SELECTOR = '//td[2]'

		for item in response.xpath(MAIN_SELECTOR):

			LINK_SELECTOR = 'a[href$=".html"] ::attr(href)'
			links.extend(item.css(LINK_SELECTOR).getall())
		# links.append('')
		with open('links_map.csv', 'a', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(links)

		self.current_page = self.get_next_page()

		if self.current_page:
			yield scrapy.Request(response.urljoin(self.main_page + self.current_page),callback=self.parse)

	def get_next_page(self):

		page = ''
		fp = open('URLs_list.txt')

		for i, line in enumerate(fp):

			if i == self.page_count:

				if i == 28:
					page = word_tokenize(line)[1] + ' ' + word_tokenize(line)[2]
				else:
					page = word_tokenize(line)[1]
				self.page_count += 1
				break

		fp.close()

		return page