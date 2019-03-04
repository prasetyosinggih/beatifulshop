from flask import Flask
import bs4 as bs
import urllib.request
import nltk
from nltk.stem import PorterStemmer
import xml.etree.ElementTree as ET

nltk.download('punkt')
nltk.download('stopwords')

from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)

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


if __name__ == "__main__":

	app.run(debug='true',port='5001')



