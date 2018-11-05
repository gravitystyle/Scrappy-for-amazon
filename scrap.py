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
	urls = {}
	wordsToSearch = []
	for category in categories:
		for license in licenses:
			wordsToSearch = [] #Reinitialize the words to search
			categorySplited = category.lower().split() #Create a list of words from the string of the category
			licenseSplited = license.lower().split() #Create a list of words from the string of the license
			wordsToSearch.extend(categorySplited) #add the list of category words to the words to search
			wordsToSearch.extend(licenseSplited) #add the list of license words to the words to search
			urls[category, license] = baseUrl + "+".join(wordsToSearch) #Create the url and add it to the dictionnary
	return urls



def exportInJson(fileName, data): # export the data in a json file
	with open(fileName,'w') as f:
		f.write(json.dumps(data))


def urlGenerator(categoryFileName, licenseFileName): #generate the urls
	categories = readFile(categoryFileName)
	licenses = readFile(licenseFileName)
	urls = createUrls(categories,licenses)
	return urls

def cleanText(text): # transform the text got on the website into a number
	numberList = [s for s in text.split() if s.isdigit()] #create a list of strings of the digit contained into the text
	return int(''.join(numberList)) #add the digit together and transgorm it into an int
	


class BlogSpider(scrapy.Spider):
	name = 'blogspider'


	def start_requests(self):
		
		masterList = urlGenerator('categories.json', 'licenses.json') #Create a list of urls crossing categories and licenses, generate json with this list

		for cle in masterList.keys():
			url = masterList[cle]
			yield scrapy.Request(url=url, callback=self.parse)



	def parse(self, response):
		for title in response.css('div#topDynamicContent'):#scrap the website page
			textCollected =title.css('span ::text').extract_first() # collect the information from the website
			yield {"test":cleanText(textCollected)} # clean the text



######Test#####
# masterList= {}
# masterList = urlGenerator('categories.json', 'licenses.json')
# for cle in masterList.keys():
# 	print(masterList[cle])
# print(type (cleanText("1-16 sur sur 20\u00a0000 r\u00e9sultats pour ")))