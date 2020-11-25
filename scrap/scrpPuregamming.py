from bs4 import BeautifulSoup 
from selenium import webdriver
import requests


#noticia

class ScrpPuregamming(object):
    
    def __init__ (self):
        self.url='https://puregaming.es/noticias/'
    
    def getNotice(self):
        try:
            page=requests.get(self.url)
            pageBeauti=BeautifulSoup(page.content,'html.parser') 
            item=pageBeauti.find('div',class_='item')
            #titulo por si lo necesitaba 
            title=item.find('div', class_='title')
            #url Articulo al final esto es lo que querian 
            urlArticle=item.find('a')
            return urlArticle['href']
        except:
            print('error en Pure gaming')
            print('error en Pure gamming')




