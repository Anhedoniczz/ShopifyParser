import requests
import json 
import pandas as pd
import colorama
from colorama import Fore
import os 
import sys
from time import sleep
import fade
import concurrent.futures
import pyfiglet

figlet = pyfiglet.figlet_format("Shopify Parser", font = "slant"  )
text = (figlet)
faded_text = fade.brazil(text)
print(faded_text)

colorama.init()

text1 = "\033[0;91m[+] This program can extract data from shopify websites."
for z in text1:
  sleep(0.02) 
  sys.stdout.write(z)
  sys.stdout.flush()
print()

link = input("\n[+] Enter the link of a shopify website : ")

url = ((link) + "/products.json")

r = requests.get(url)

data = r.json()

product_list = []

for item in data['products']:
    id = item["id"]
    title = item['title']
    handle = item['handle']
    createdate = item['created_at']
    for image in item['images']:
        try:
            imagesrc = image['src']
        except:
            image = 'None'
    for variant in item['variants']:
        color = variant['option1']
        size = variant['option2']
        sku = variant['sku']
        available = variant['available']
        price = variant['price']
        weight = variant['grams']

        product = {
            'id' : id,
            'title' : title,
            'handle' : handle,
            'createdate' : createdate,
            'image' : imagesrc,
            'price' : price,
            'color' : color,
            'size' : size,
            'sku' : sku,
            'available' : available,
            'weight' : weight

        }

        product_list.append(product)

dataframe = pd.DataFrame(product_list)

filename = input("\n[+] What do you want to name your file : ")
dataframe.to_csv((filename) + '.csv')

print("\n[+] Data saved to " + (filename) + '.csv')