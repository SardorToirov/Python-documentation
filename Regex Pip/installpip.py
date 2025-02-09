#googletrans
# from googletrans import Translator
#t = Translator()
# while True:
#     matn = input("tarjimon uz-en: ")
#     if matn == "exit":
#         break
#     matn_eng = t.translate(matn, dest="en")
#     print(matn_eng.text)
#     continue

# ----------------------------------------------------


# import asyncio
# from googletrans import Translator
# async def main():
#     translator = Translator()
#     matn_eng = await translator.translate("salom", dest="en")
#     print(matn_eng.text)
#
# asyncio.run(main())



# requests

# import requests
# zapros = requests.get("https://kun.uz")
# print(zapros.text)

# -----------------------------------------------------
# Web Scraping

# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://kun.uz/news/main")
#
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
# news = soup.find_all(class_="news-title")
# j = 1
# print("\n\tushbu ma'lumotlar: https://kun.uz/news/main web saytan olinmoqda:) \n")
# print(news)
# while True:
#     if j == 10:
#         break
#     else:
#         print(news[j].text)
#     j+=1

# import requests
# from bs4 import BeautifulSoup

# Fetch the webpage
# url = "https://kun.uz/news/main"
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title")
# print(news[1].text.strip())





