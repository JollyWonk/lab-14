import requests
from bs4 import BeautifulSoup
import json

def count_keywords(url, keywords):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text().lower() 

    keyword_counts = {}
    for keyword in keywords:
        count = text.count(keyword.strip().lower())  
        keyword_counts[keyword] = count


    if any(keyword_counts.values()):
        with open('keyword_counts.json', 'w', encoding='utf-8') as f:
            json.dump(keyword_counts, f, ensure_ascii=False, indent=4)
        print("Результати збережено в 'keyword_counts.json'")
    else:
        print("Ключові слова не знайдені на сторінці.")


keywords_input = input("Введіть ключові слова для підрахунку, розділені комами: ")
keywords_list = [word.strip() for word in keywords_input.split(",")]  

url = input("Введіть URL-адресу веб-сторінки: ")

count_keywords(url, keywords_list)
