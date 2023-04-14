import requests
from bs4 import BeautifulSoup
import json
import lxml

def get_data(url):
	headers = {
		"Accept" : "*/*",
		"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
	}

	req = requests.get(url, headers)
	# print(req.text)

	# with open("projects.html", "w", encoding="utf-8") as file:
	# 	file.write(req.text)

	with open("projects.html", "r", encoding="utf-8") as file:
		src = file.read()

	soup = BeautifulSoup(src, "lxml")

	articles = soup.find("div", class_="listing-main-block")
	# print(articles)
	for article in articles:
		product_title = soup.find("div", class_="category-block").find("div", "title").find("div", "name").text
		product_name = soup.find("div", class_="category-block").find("div", "category-block-content-item").find("div", "main-image").find("div", "bottom-info").find("div", "main-title").text.strip()
		product_price = soup.find("div", class_="category-block").find("div", "category-block-content-item").find("div", "main-image").find("div", "modal-main-image hidden").find("div", "modal-main-price").find("span").text
		product_url = soup.find("div", class_="category-block").find("div", "category-block-content").find("div", "category-block-content-item").find("a").get("href")
		print(product_title, product_name, product_price, f"https://www.mashina.kg{product_url}")

get_data("https://www.mashina.kg/")