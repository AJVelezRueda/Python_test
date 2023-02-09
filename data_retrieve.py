import requests

def get_next_items(next_url):
    data = requests.get(next_url).json()
    results = list(set([x["manufacturer"].title() for x in data["results"]]))
    next_url = data["next"]
    return (results, next_url) 

def retrieve_api_data():
    query_result, next_item_url = get_next_items("https://swapi.dev/api/vehicles/")
    items = query_result
    items_list_len = len(items)
    
    if  items_list_len >= 5:
        return items[0:5]
    else:
        while len(items) <= 5:
            next_items, next_item_url = get_next_items(next_item_url)
            items += next_items

        return items[0:5]

if __name__ == "__main__":
    print (retrieve_api_data())
