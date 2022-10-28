from inspect import classify_class_attrs
from re import T
from bs4 import BeautifulSoup
import requests 
import time
#allow user to search information about an specific president 
print("About which LaLiga president do you want to know about?")
presidente = input('type his/her name: ')
print(f"filtrando {presidente}")

#create function 
def fin_news():
    #get marca website 
    html_text = requests.get('https://www.marca.com/futbol.html?intcmp=MENUPROD&s_kw=futbol').text
    #using beautiful soup libraries
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('div',class_ = 'ue-c-cover-content__main')
    #enumerate the new with the index variable
    for index, new in enumerate(news):
        Titulo = new.find('h2', class_ = 'ue-c-cover-content__headline').text
        if presidente in Titulo:
            #if the president name is in any of the new then give me name of the team, name of the writer and the link to the new
            Tname = new.find('div',class_ = 'ue-c-cover-content__kicker-group').text.replace('','')
            Aname = new.find('span', class_ = 'ue-c-cover-content__byline-name').text
            more_info = new.header.a['href']
            #store information into posts file 
            with open('posts/{index}.txt', 'w') as f:
                   f.write(f"Noticia del equipo: {Tname.strip()}\n ")
                   f.write(f"ecrita por: {Aname.strip()} \n")
                   f.write(f"con el Titulo: {Titulo} \n ")
                   f.write(f"More info: {more_info}")
            print(f'file saved: {index}')
#setting time to re run the program in 10 minutes
if __name__ == '__main__':
    while True:
        fin_news()
        time_wait = 10
        print(f'waiting {time_wait} minutes')
        time.sleep(time_wait * 60)
