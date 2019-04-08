import scrapy
import os

class MathprofiSpider(scrapy.Spider):
	name = "mathprofi_spider"
	start_urls = ['http://mathprofi.ru/']

	# urls = []
	links = {}
	# urls.append('mathprofi.ru')
	urls.append(start_urls[0])
	urls_counter = 0
	fisrt_run = True

	def parse(self, response):

		if (self.fisrt_run):
			SET_SELECTOR = '.classs'
			for page in response.css(SET_SELECTOR):
				NAME_SELECTOR = 'a ::attr(href)'
				links[response.request.url] = page.css(NAME_SELECTOR).getall()
				# self.urls.extend(page.css(NAME_SELECTOR).getall())
				yield {
	                'name': page.css(NAME_SELECTOR).getall(),
	            }
			try:
				os.mkdir('links')
			except FileExistsError:
    			print("Directory " , dirName ,  " already exists")
			# limited_list = self.urls[:100]
			limited_list = self.links[:100]
			# with open('URLs_list.txt', 'w') as f:
			for item in limited_list.items():
				# f.write("№%i " % limited_list.index(item))
				with open('links/' + item + '.txt', 'w+') as f:
					for value in item.values():
						f.write((start_urls[0] + "%s\n" % value))
			self.fisrt_run = False

		texts = []

		TEXT_SELECTOR = './/td[2]/p/text()'
		for text in response.xpath(TEXT_SELECTOR):
			texts.append(text.get())
			yield {
				'text': text.get(),
			}

		with open('№' + str(self.urls_counter) + '_' + self.urls[self.urls_counter] + '.txt', 'w') as f:
			for item in texts:
				f.write("%s\n" % item)

		self.urls_counter += 1
		next_page = self.start_urls[0] + self.urls[self.urls_counter]
		if next_page:
			yield scrapy.Request(response.urljoin(next_page),callback=self.parse)
