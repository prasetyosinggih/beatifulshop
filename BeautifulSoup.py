#BeautifulSoup
from flask import Flask
import simplejson as json
import bs4 as bs
import urllib.request

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

if __name__ == "__main__":

	app.run(debug='true',port='5001')



