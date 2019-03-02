from flask import Flask
import simplejson as json
import bs4 as bs
import pandas as pd
import urllib.request
import nltk
from nltk.stem import PorterStemmer
import xml.etree.ElementTree as ET
import json

nltk.download('punkt')
nltk.download('stopwords')

from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)

@app.route('/')

def index():
	myUrl = "http://www.dkantin.com/?s=sayur&category=&post_type=product"
	uClient = urllib.request.urlopen(myUrl).read()

	soup = bs.BeautifulSoup(uClient,'html.parser')
	containers = soup.findAll("li",{"class":"product"})


	for container in containers:
		
		ti_container = container.findAll("h2",{"class":"woocommerce-loop-product__title"})
		product_name = ti_container[0].text

		ha_container = container.findAll("span",{"class":"woocommerce-Price-amount"})
		harga_product = ha_container[0].text

		harga = harga_product.replace('Rp','').replace(',','').replace('.','')

		print("Product :" + product_name)
		print("Harga :" + harga)

	return "hasil"


@app.route('/bukalapak')
def bukalapak():
	myUrl = "https://www.bukalapak.com/c/handphone/hp-smartphone/m-iphone?from=omnisearch&search_source=omnisearch_redirect"
	uClient = urllib.request.urlopen(myUrl).read()

	soup = bs.BeautifulSoup(uClient,'html.parser')
	containers = soup.findAll("div",{"class":"o-layout__item u-2of12 u-mrgn-bottom--3"})


	for container in containers:
		ti_container = container.findAll("a",{"class":"c-product-card__name js-tracker-product-link"})
		product_name = ti_container[0].text

		ha_container = container.findAll("span",{"class":"amount positive"})
		harga_product = ha_container[0].text

		print("Product : " + product_name)
		print("Harga : " + harga_product)

	return "Hasil BukaLapak"


@app.route('/jdid')
def jdid():
	myUrl=urllib.request.urlopen("https://www.jd.id/search?keywords=samsung").read()
	soup = bs.BeautifulSoup(myUrl,'html.parser')
	maxpage = soup.findAll("input",{"id":"mytotalPage"})
	total_max = str(maxpage[0]['value'])
	#print(total_max)

	par = int(total_max)
	for param in range(1,par):
		keywords = str(param)
		myUrl=urllib.request.urlopen("https://www.jd.id/search?keywords=samsung&page="+keywords+"").read()
		soup = bs.BeautifulSoup(myUrl,'html.parser')
		containers = soup.findAll("li",{"class":" "})

		for container in containers:
			titel_container = container.findAll("a",{"class":"name"})
			product_name = titel_container[0].text

			harga_container = container.findAll("span",{"eptid":"price"})
			harga_name = harga_container[0].text
			harga = harga_name.replace(',','').replace('Rp','').replace(' ','')

		print("Product : " + product_name)
		print("Harga : " + harga)
		print("Page : " + keywords)

	return "Hasil JDID"


@app.route('/jd')
def jd():

	myUrl=urllib.request.urlopen("https://www.jd.id/search?keywords=samsung").read()
	soup = bs.BeautifulSoup(myUrl,'html.parser')
	maxpage = soup.findAll("input",{"id":"mytotalPage"})
	total_max = str(maxpage[0]['value'])
	#print(total_max)
	
	par=int(total_max)
	for param in range(1,par):
			
			keywords=str(param)
			myUrl=urllib.request.urlopen("https://www.jd.id/search?keywords=samsung&page="+keywords+"").read()
			soup = bs.BeautifulSoup(myUrl,'html.parser')
			containers = soup.findAll("li",{"class":" "})

			for container in containers:
				titel_container = container.findAll("a",{"class":"name"})
				product_name = titel_container[0].text

				harga_container = container.findAll("span",{"eptid":"price"})
				harga_name = harga_container[0].text
				harga = harga_name.replace(',','').replace('Rp','').replace(' ','')
				
				if int(harga) >= 4000000 :
					 
					print("Product  = "+ product_name)
					print("Harga    = "+ harga)
					print("Page     = "+ keywords)
					print("Max Page = "+ total_max)
				
	return "Hasil JDID"


@app.route('/evoware')
def evoware():
	myUrl=urllib.request.urlopen("http://www.evoware.id/home/blog_post/1").read()
	soup = bs.BeautifulSoup(myUrl,'html.parser')
	containers = soup.findAll("div",{"class":"row flex-items-md-center"})

	blog = containers[0].text
	print(blog)

	stopWords = set(stopwords.words('english'))
	words = word_tokenize(blog)
	wordsFilter = []

	for w in words:
		if w not in stopWords:
			wordsFilter.append(w)

	#print(wordsFilter)
	json.dumps(wordsFilter)
	

	return "Hasil Blog"


@app.route('/evo')
def evo():
	myUrl = urllib.request.urlopen("http://www.evoware.id/home/our_blog")
	soup = bs.BeautifulSoup(myUrl,'html.parser')
	containers = soup.findAll("div",{"class":"col-xs-12 col-md-6 col-lg-4","class":"js-isotope__item"})

	for par in range(1,len(containers)):
		myUrl=urllib.request.urlopen("http://www.evoware.id/home/blog_post/"+str(par)).read()
		soup = bs.BeautifulSoup(myUrl,'html.parser')
		containers = soup.findAll("div",{"class":"row flex-items-md-center"})

		blog = containers[0].text
		print(blog)

		stopWords = set(stopwords.words('english'))
		#words = sent_tokenize(blog)
		words = word_tokenize(blog)
		wordsFilter = []

		for w in words:
			if w not in stopWords:
				wordsFilter.append(w)

		print(wordsFilter)

			
	return "Hasil Evoware"

@app.route('/stem')
def stem():
	myUrl = urllib.request.urlopen("http://www.evoware.id/home/our_blog")
	soup = bs.BeautifulSoup(myUrl,'html.parser')
	containers = soup.findAll("div",{"class":"col-xs-12 col-md-6 col-lg-4","class":"js-isotope__item"})

	for par in range(1,len(containers)):
	
		myUrl=urllib.request.urlopen("http://www.evoware.id/home/blog_post/"+str(par)).read()
		soup = bs.BeautifulSoup(myUrl,'html.parser')
		containers = soup.findAll("div",{"class":"row flex-items-md-center"})

		blog = containers[0].text
		print(blog)

		stopWords = set(stopwords.words('english'))
		#words = sent_tokenize(blog)
		words = word_tokenize(blog)
		wordsFiltered = []
		total = []
		ps = PorterStemmer()
		 
		for w in words:
		    if w not in stopWords:
		        wordsFiltered.append(w)
		
		for word in wordsFiltered:
			total.append(ps.stem(word))
			#tree = ET.ElementTree(ET.fromstring(ps.stem(word).strip(".,:-''_").replace("", "")))
			#d = json.loads(ps.stem(word).strip(".,:-''_"))
		#print json.dumps(d['glossary'])
		print(total)
		    
	return "Hasil Stem"



if __name__ == "__main__":

	app.run(debug='true',port='5001')



