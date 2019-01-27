# importing required packages
from bs4 import BeautifulSoup
from zipfile import ZipFile
from constants import *
import pandas as pd
import requests
import urllib
import shutil
import redis
import os

path = os.getcwd() + '/cherry_app'
db = redis.StrictRedis(host=DB_HOST, port=DB_PORT, db=DB_NO, password=PASSWORD)

def generate_bhav_url():
	try:
		html = urllib.urlopen(BSE_URL)
		soup = BeautifulSoup(html, 'html.parser')
		bhav_url = soup.find("a", {"id": "ContentPlaceHolder1_btnhylZip"})["href"]
		zip_name = bhav_url[bhav_url.rfind("/") + 1:]
		csv_file = zip_name[0:zip_name.find("_")] + '.CSV'
		return bhav_url, zip_name, csv_file

	except Exception as e:
		print e.message

def download_equity_zip(bhav_url, zip_name):
	try:
		r = requests.get(bhav_url) # create HTTP response object
		with open(path + '/data/' + zip_name,'wb') as f: 
		    f.write(r.content)

	except Exception as e:
		print e.message

def extract_zip(zip_name):
	try:
		# opening the zip file in READ mode 
		with ZipFile(path + '/data/' + zip_name, 'r') as zip:
			zip.extractall(path + '/data/')
	except Exception as e:
		print e.message


def write_to_redis(csv_file):
	try:
		df = pd.read_csv(path + '/data/' + csv_file)
		db.set("bhav", df.to_msgpack(compress='zlib'))
	except Exception as e:
		print e.message


if __name__ == "__main__":
	# clear data folder
	shutil.rmtree(path + '/data/')
	os.makedirs(path + '/data/')

	bhav_url, zip_name, csv_file = generate_bhav_url()
	download_equity_zip(bhav_url, zip_name)
	extract_zip(zip_name)
	write_to_redis(csv_file)
