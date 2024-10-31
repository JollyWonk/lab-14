import requests
import json
import random

def get_random_quote():
    url = "http://api.forismatic.com/api/1.0/"
    params = {
        "method": "getQuote",
        "format": "json",
        "lang": "en"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Помилка при отриманi цитати: {e}")
        return None

def save_quotes_to_file(num_quotes, filename="quotes.json"):
    quotes = []
    for _ in range(num_quotes):
        quote = get_random_quote()
        if quote:
            quotes.append(quote)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)
    print(f"Цитата успiшно в файлi {filename}")

save_quotes_to_file(5)
