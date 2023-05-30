import requests
from bs4 import BeautifulSoup
import csv
import time


base_url = 'https://www.juventasport.com/products?type_id=11316&family_id=9654&page='
current_page = 1

with open('juventa.csv', "w", encoding='utf-8') as textfile:
    writer = csv.writer(textfile)
    writer.writerow(["Rb.", "Artikal", "Cijena"])

count_items = 0
total_items_req = base_url + str(current_page)
juventa_req = requests.get(total_items_req)
juventa_req_soup = BeautifulSoup(juventa_req.text, 'html.parser')
juventa_req_soup.prettify()

all_brands = juventa_req_soup.findAll('div', {'class': 'webshop'})
number_of_brands = 0
for brand in all_brands:
    count = brand.findAll('span', {'class': 'social_bar_content'})
    real_count = int(count[0].text)
    number_of_brands += real_count

while current_page < (number_of_brands/33):
    print("======================================================================================================")
    print("Upisano: " + str(current_page * 2))

    url = base_url + str(current_page)
    juventa_r = requests.get(url)
    juventa_soup = BeautifulSoup(centrum_r.text, 'html.parser')
    juventa_soup.prettify()

    all_content = juventa_soup.findAll('div', {'class': 'row'})
    try:
        with open('juventa.csv', "a", encoding='utf-8') as textfile:
            writer = csv.writer(textfile)
            for link in all_content:
                name = link.findAll('a', {'class': 'klikni product-item-link'})
                price = link.findAll('span', {'class': 'price'})
                if price:
                    writer.writerow([count_items+1, name[0].text, price[0].text])
                    print(name[0].text + " " + price[0].text)
                count_items += 1
            current_page += 1
            # time.sleep(3)
    except Exception as e:
        print(e)

