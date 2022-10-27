from inspect import classify_class_attrs
from re import T
from bs4 import BeautifulSoup
import requests 
import time

print("quieres buscar informacion de algun presidente?")
presidente = input('>')
print(f"filtrando {presidente}")

def fin_news():
    html_text = requests.get('https://www.marca.com/futbol.html?intcmp=MENUPROD&s_kw=futbol').text
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('div',class_ = 'ue-c-cover-content__main')

    for index, new in enumerate(news):
        Tname = new.find('div',class_ = 'ue-c-cover-content__kicker-group').text.replace('','')
        if 'FC Barcelona' in Tname:
            Aname = new.find('span', class_ = 'ue-c-cover-content__byline-name').text
            Titulo = new.find('h2', class_ = 'ue-c-cover-content__headline').text
            more_info = new.header.a['href']
            if presidente in Titulo:
                with open('posts/{index}.txt', 'w') as f:
                   f.write(f"Noticia del equipo: {Tname.strip()}\n ")
                   f.write(f"ecrita por: {Aname.strip()} \n")
                   f.write(f"con el Titulo: {Titulo} \n ")
                   f.write(f"More info: {more_info}")
                print(f'file saved: {index}')
if __name__ == '__main__':
    while True:
        fin_news()
        time_wait = 10
        print(f'waiting {time_wait} minutes')
        time.sleep(time_wait * 60)
