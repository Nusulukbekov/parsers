import requests
from bs4 import BeautifulSoup
import lxml
import json

headers = {
	"Accept" : "*/*",
	"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

fests_urls_list = []

for i in range (0, 24, 24):
	url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=&to_date=&maxprice=500&o={i}&bannertitle=May"
	# print(url)

	# Наверное основная фишка была в отправке запросов через прокси, но мы то не Россия и нас не касаются санкции

	req = requests.get(url=url, headers=headers)

	json_data = json.loads(req.text)

	html_response = json_data["html"]

	with open(f"data/index_{i}.html", "w", encoding="utf-8") as file:
		file.write(html_response)

	with open(f"data/index_{i}.html", "r", encoding="utf-8") as file:
		src = file.read()

	soup = BeautifulSoup(src, "lxml")

	cards = soup.find("a", class_="card-details-link")

	for item in cards:
		fests_url = f"https://www.skiddle.com" + item.get("href")
		fests_urls_list.append(fests_url)

# print(fests_urls_list)

for url in fests_urls_list:
	req = requests.get(url=url, headers=headers)

	try:
		soup = BeautifulSoup(req.text, "lxml")

		fest_info_block = soup.find("div", class_="MuiGrid-root MuiGrid-container")
		fests_name = soup.find("div", class_="uiContainer-root MuiContainer-maxWidthFalse").find("h1", class_="MuiTypography-root MuiTypography-body1").text.strip()
		print(fest_info_block)

	except Exception as ex:
		print(ex)
		print("error, not 404 lol")