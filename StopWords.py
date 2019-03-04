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

