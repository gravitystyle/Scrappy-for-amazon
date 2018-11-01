import scrapy
import json


# def main():
#     name = 'blogspider'
#     start_urls = ['https://www.amazon.fr/s/ref=nb_sb_noss_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=mug+harry+potter']

#     for title in response.css('div#topDynamicContent span#s-result-count'):
#     	print(title.css('span ::text').extract_first())

def cleanText(text):
	words = text.split()


def readFile(fileName): #extract a list from a json file -- use to create a list of category and licenses
	with open(fileName,'r') as file:
		data = json.load(file)
	return data



class BlogSpider(scrapy.Spider):
	name = 'blogspider'

	def start_requests(self):
		
		urls = [
			'https://www.amazon.fr/s/ref=a9_asi_1?rh=i%3Aaps%2Ck%3Amug+batman&keywords=mug+batman',
			'https://www.amazon.fr/s/ref=nb_sb_noss_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=porte+cl%C3%A9+batman',
			'https://www.amazon.fr/s/ref=nb_sb_noss?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=tartendkzjqsldjk'
		] #URL to scrap

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		for title in response.css('div#topDynamicContent'):#scrap the website page
			yield {"test":title.css('span ::text').extract_first()} # extract the sentence


