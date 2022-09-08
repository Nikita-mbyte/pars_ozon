import json
import glob
import re
from pandas import Ha

fdsfds
fsdf
def get_products() -> list:
    return glob.glob('products/*.html')

def get_json(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        return json.loads(data)

def parse_data(data: dict) -> dict:
    widgets = data.get('widgetStates')
    for key, value in widgets.items():
        if 'webProductHeading' in key:
            title = json.loads(value).get('title')
        if 'webSale' in key:
            prices = json.loads(value).get('offers')[0]
            if prices.get('price'):
                price = re.search(r'[0-9]+', prices.get('price').replace(u'\u2009', ''))[0]
            else:
                price = 0
            if prices.get('originalPrice'):
                discount_price = re.search(r'[0-9]+', prices.get('originalPrice').replace(u'\u2009', ''))[0]
            else:
                discount_price = 0

    layout = json.loads(data.get('layoutTrackingInfo'))
    brand = layout.get('brandName')
    category = layout.get('categoryName')
    sku = layout.get('sku')
    url = layout.get('currentPageUrl')

    product = {
        'title': title,
        'price': price,
        'discount_price': discount_price,
        'brand': brand,
        'category': category,
        'sku': sku,
        'url': url
    }
    return product


def main():

    # result_filename = 'ozon_result.csv'
    # csvHandler(result_filename).create_headers_csv_semicolon(['title', 'price',
    #                                                  'discount_price', 'brand', 'category', 'sku', 'url'])
    products = get_products()
    for product in products:
        try:
            product_json = get_json(product)
            result = parse_data(product_json)
            print(result)
            # csvHandler(result_filename).write_to_csv_semicolon(result)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()