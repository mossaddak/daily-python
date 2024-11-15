import requests

def check_api(currency_from, currency_to):
    url = f"https://api.exchangerate-api.com/v4/latest/{currency_from}"
    response = requests.get(url).json()    
    return response.get("rates", {}).get(currency_to)

print(check_api("USD", "BDT"))