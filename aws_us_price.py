import requests
import json
import pathlib

local_index_file = pathlib.Path("aws_us_price_index.json")
if not local_index_file.exists():
    index_res = requests.get('https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json')
    index_res.raise_for_status()
    with open('aws_us_price_index.json', 'wb') as index_file:
        for chunk in index_res.iter_content():
            index_file.write(chunk)

with open("aws_us_price_index.json", encoding='utf-8') as file:
    index_info = json.load(file)
    for key in list(index_info['offers'].keys()):
        print(key)