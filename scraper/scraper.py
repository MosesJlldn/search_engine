import scrapy

class MathprofiSpider(scrapy.Spider):
	name = "mathprofi_spider"
	start_urls = ['http://mathprofi.ru/']

	urls = []
	urls.append('mathprofi.ru')
	urls_counter = 0
	fisrt_run = True

	def parse(self, response):

		if (self.fisrt_run):
			SET_SELECTOR = '.classs'
			for page in response.css(SET_SELECTOR):
				NAME_SELECTOR = 'a ::attr(href)'
				self.urls.extend(page.css(NAME_SELECTOR).getall())
				yield {
	                'name': page.css(NAME_SELECTOR).getall(),
	            }

			limited_list = self.urls[:100]
			with open('URLs_list.txt', 'w') as f:
				for item in limited_list:
					f.write("№%i " % limited_list.index(item))
					f.write("%s\n" % item)

			self.fisrt_run = False

		texts = ['URLs_list.txt']

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