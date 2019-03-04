from flask import Flask
import urllib.request
import bs4 as bs
import nltk
from nltk.stem import PorterStemmer
import json


nltk.download('punkt')
nltk.download('stopwords')

from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


app=Flask(__name__)

@app.route('/dkantin')

def dkantin():
	myUrl = "http://www.dkantin.com/?s=sayur&category=&post_type=product"
	uClient=urllib.request.urlopen(myUrl).read()
	soup=bs.BeautifulSoup(uClient,'html.parser')
	
	container=soup.findAll("li",{"class":"product"})

	for containers in container:
		#print(containers)
		ti_container=containers.findAll("h2",{"class":"woocommerce-loop-product__title"})
		produk_name=ti_container[0].text
		
		ha_container = containers.findAll("span",{"class":"woocommerce-Price-amount amount"})
		harga_produk=ha_container[0].text.replace('Rp','').replace(',','').replace('.00','')

		print(produk_name)
		print(harga_produk)


@app.route('/evoware')
def evoware():
	myUrl=urllib.request.urlopen("http://www.evoware.id/home/blog_post/1").read()
	soup=bs.BeautifulSoup(myUrl,'html.parser')
	containers=soup.findAll("div",{"class":"row flex-items-md-center"})

	blog = containers[0].text
	print(blog)	

	stopWords = set(stopwords.words('english'))
	words = word_tokenize(blog)
	wordFilter = []

	for w in words:
		if w not in stopWords:
			w.replace(',','')
			wordFilter.append(w)


	print(wordFilter)
	json.dumps(wordFilter)


	return "Hasil Dkantin"


@app.route('/stemer')
def stemer():
	myUrl=urllib.request.urlopen("http://www.evoware.id/home/blog_post/1").read()
	soup=bs.BeautifulSoup(myUrl,'html.parser')
	containers=soup.findAll("div",{"class":"row flex-items-md-center"})

	blog = containers[0].text
	print(blog)	

	stopWords = set(stopwords.words('english'))
	words = word_tokenize(blog)
	wordsFiltered = []
	total = []
	ps = WordNetLemmatizer()
	 
	for w in words:
	    if w not in stopWords:
	        wordsFiltered.append(w)
		
	for word in wordsFiltered:
		total.append(ps.lemmatize(word,pos='a'))
		#tree = ET.ElementTree(ET.fromstring(ps.stem(word).strip(".,:-''_").replace("", "")))
		#d = json.loads(ps.stem(word).strip(".,:-''_"))
	
	#print json.dumps(d['glossary'])
	print(total)

	print(ps.lemmatize("Sustainable"))
	print(ps.lemmatize("better",pos='a'))
	print(ps.lemmatize("cats"))


	return "Hasil Dkantin"


if __name__ == "__main__":
	app.run(debug="true",port="5005")