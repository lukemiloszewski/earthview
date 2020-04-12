import urllib.request
import csv
import random
import sys

with open('earthview.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    address_list = []

	# extract each line from the .csv file and store in a list
    for row in csv_reader:
        address_list.append(row)
    
    # generate a random sample from the collection and download them
    download_list = random.sample(address_list, int(sys.argv[1]))
    for row in download_list:
        urllib.request.urlretrieve(row[0], "image/" + row[1] + ", " + row[2] + "," + row[3] + ".jpg")
