from bs4 import BeautifulSoup 
from selenium import webdriver
import requests


#noticia

class ScrpPuregamming(object):
    
    def __init__ (self):
        self.url='https://puregaming.es/noticias/'
    
    def getNotice(self):
        page=requests.get(self.url)
        pageBeauti=BeautifulSoup(page.content,'html.parser') 
        item=pageBeauti.find('div',class_='item')
        #imagen por si la necesitaba 
        img=item.find('img')
        
        #titulo por si lo necesitaba 
        title=item.find('div', class_='title')
        
        #url Articulo al final esto es lo que querian 
        urlArticle=item.find('a')
        print(urlArticle['href'])
        return urlArticle['href']




