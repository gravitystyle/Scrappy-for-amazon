import scrapy
import json


def readFile(fileName): #extract a list from a json file -- use to create a list of category and licenses
	with open(fileName,'r') as file:
		data = json.load(file)
	return data

def createAmazonUrls(categories, licenses): # create the research Urls links for Amazon --- Have to be changed for another website
	baseUrl = "https://www.amazon.fr/s/ref=nb_sb_noss_1?__mk_fr_FR=ÅMÅŽÕÑ&url=search-alias%3Daps&field-keywords=" #This is the base use for the Amazon Url
	urls = []
	wordsToSearch = []
	for category in categories:
		for license in licenses:
			wordsToSearch = [] #Reinitialize the words to search
			categorySplited = category.lower().split() #Create a list of words from the string of the category
			licenseSplited = license.lower().split() #Create a list of words from the string of the license
			wordsToSearch.extend(categorySplited) #add the list of category words to the words to search
			wordsToSearch.extend(licenseSplited) #add the list of license words to the words to search
			urls.append(baseUrl + "+".join(wordsToSearch)) #Create the url and add it to the list of urls
	return urls


def exportInJson(fileName, data): # export the data in a json file
	with open(fileName,'w') as f:
		f.write(json.dumps(data))



# class BlogSpider(scrapy.Spider):
# 	name = 'blogspider'

# 	def start_requests(self):
		
# 		urls = [
# 			'https://www.amazon.fr/s/ref=a9_asi_1?rh=i%3Aaps%2Ck%3Amug+batman&keywords=mug+batman',
# 			'https://www.amazon.fr/s/ref=nb_sb_noss_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=porte+cl%C3%A9+batman',
# 			'https://www.amazon.fr/s/ref=nb_sb_noss?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=tartendkzjqsldjk'
# 		] #URL to scrap

# 		for url in urls:
# 			yield scrapy.Request(url=url, callback=self.parse)

# 	def parse(self, response):
# 		for title in response.css('div#topDynamicContent'):#scrap the website page
# 			yield {"test":title.css('span ::text').extract_first()} # extract the sentence


######Test the collection of categories and licenses####
# cat = readFile('categories.json')
# lic = readFile('licenses.json')
# urls = createAmazonUrls(cat,lic)
# exportInJson("testUrl.json",urls)
# print (len(urls))