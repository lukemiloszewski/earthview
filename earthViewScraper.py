import requests
import urllib.request
from bs4 import BeautifulSoup
import csv

with open('earthview.csv', mode='w') as earthViewCSV:
    earthViewCSV = csv.writer(earthViewCSV, delimiter=',')
    address_list = []

    next_URL = None
    next_image = "/the-sill-australia-2062"

    while next_URL != "/the-sill-australia-2062":

		# construct the URL for the page that displays the image
        base_URL = 'https://earthview.withgoogle.com'
        image_URL = str(next_image)
        URL = base_URL + image_URL

		# create a BeautifulSoup object of the webpage
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

		# extract the image URL, the region name and the country name of the associated image
        current_image = soup.find('img', class_='photo-view photo-view--1 photo-view--active').get('src')
        region = soup.find('div', class_='location__region').text
        country = soup.find('div', class_='location__country').text

		# determine the URL of the next image to be displayed
        next_image = soup.find('a', class_='pagination__link pagination__link--next').get('href')
        next_URL = next_image

        # extract the image number from URL
        begin_index = current_image.rfind("/") + 1
        end_index = current_image.rfind(".")
        address_list.append([int(current_image[begin_index:end_index]), country, region])
    
    address_list.sort()

    for address in address_list:
        earthViewCSV.writerow(["https://www.gstatic.com/prettyearth/assets/full/" + str(address[0]) + ".jpg", address[1], address[2], str(address[0])])
