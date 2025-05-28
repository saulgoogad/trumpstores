import requests

def get_shop_data():
    url = "https://fortnite-api.com/v2/shop/br?language=ru"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Fortnite API Error:", response.status_code)
        return []

    data = response.json()
    if 'data' not in data or 'featured' not in data['data']:
        print("Fortnite API response structure is invalid.")
        return []

    items = []
    for entry in data['data']['featured']['entries']:
        for item in entry['items']:
            items.append({
                'name': item['name'],
                'price': entry['regularPrice'],
                'image_url': item['images']['icon']
            })

    return items
