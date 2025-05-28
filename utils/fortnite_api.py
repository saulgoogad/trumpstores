import requests

def get_shop_data():
    url = "https://fortnite-api.com/v2/shop/br?language=ru"
    response = requests.get(url)
    data = response.json()
    items = []

    for entry in data['data']['featured']['entries']:
        for item in entry['items']:
            items.append({
                'name': item['name'],
                'price': entry['regularPrice'],
                'image_url': item['images']['icon']
            })

    return items