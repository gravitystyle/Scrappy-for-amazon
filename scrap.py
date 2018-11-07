#! /usr/bin/env python3
# coding: utf-8

import scrapy
import json


def readFile(fileName): #extract a list from a json file -- use to create a list of category and licenses
	with open(fileName,'r') as file:
		data = json.load(file)
	return data

def createUrls(categories, licenses): # create a dictionnary of the research Urls links for Amazon --- Have to be changed for another website
	baseUrl = "https://www.amazon.fr/s/ref=nb_sb_noss_1?__mk_fr_FR=ÅMÅŽÕÑ&url=search-alias%3Daps&field-keywords=" #This is the base use for the Amazon Url
	urls = []
	wordsToSearch = []
	catLic = []
	for category in categories:
		for license in licenses:
			url = ''
			wordsToSearch = [] #Reinitialize the words to search
			categorySplited = category.lower().split() #Create a list of words from the string of the category
			licenseSplited = license.lower().split() #Create a list of words from the string of the license
			wordsToSearch.extend(categorySplited) #add the list of category words to the words to search
			wordsToSearch.extend(licenseSplited) #add the list of license words to the words to search
			catLic.append([category,license])
			url = baseUrl + "+".join(wordsToSearch) #create the url
			urls.append(url) #add url to the list
	return urls, catLic



def exportInJson(fileName, data): # export the data in a json file
	with open(fileName,'w') as f:
		f.write(json.dumps(data))


def urlGenerator(categoryFileName, licenseFileName): #generate the urls
	categories = readFile(categoryFileName)
	licenses = readFile(licenseFileName)
	urls, catLic = createUrls(categories,licenses)
	return urls, catLic

def cleanText(text): # transform the text got on the website into a number
	numberList = [s for s in text.split() if s.isdigit()] #create a list of strings of the digit contained into the text
	return int(''.join(numberList)) #add the digit together and transgorm it into an int
	


class BlogSpider(scrapy.Spider):
	name = 'blogspider'
	custom_settings = {'CONCURRENT_REQUESTS':'1'} #'DOWNLOAD_DELAY':'0.25',

	urls = []
	catLic = []


	def __init__(self):
		self.urls, self.catLic = urlGenerator('categories.json', 'licenses.json') #Create a list of urls crossing categories and licenses, generate json with this list
		# exportInJson("urls.json",[x for x in self.masterList.values()])


	def start_requests(self):
		
		for url in self.urls:
			yield scrapy.Request(url=url, callback=self.parse)



	def parse(self, response):
		for title in response.css('div#topDynamicContent'):#scrap the website page based on the css tag
			textCollected = title.css('span ::text').extract_first() # collect the information from the website
			yield {'test': cleanText(textCollected)} # clean the text



# if __name__ == '__main__':
# 	scrapper = BlogSpider()
# 	test=[]
# 	test = scrapper.start_requests()
# 	print(test)
	


######Test#####
# urls = []
# catLic = []
# urls, catLic = urlGenerator('categories.json','licenses.json')
# print(urls, catLic)
# print(len(urls)," = ", len(catLic))