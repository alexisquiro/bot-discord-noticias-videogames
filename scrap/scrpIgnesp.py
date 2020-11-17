
from bs4 import BeautifulSoup 
from selenium import webdriver
import requests

#xbox y ps5 

class ScrpIgnesp(object):
    
    def __init__ (self):
        self.urlxbox='https://es.ign.com/xbox-series-x'
        self.urlps5='https://es.ign.com/ps5'

    def getNoticexbox(self):
        page=requests.get(self.urlxbox)
        pageBeauti=BeautifulSoup(page.content,'html.parser') 
        #extraemos el titulo por si lo necesitaban 
        title=pageBeauti.find('article',class_='card PREVIEW p1')
        a=title.find('a')
        #del mismo a se extrae el url el url es lo que quieren 
        #no se une con el otro link porque ya lo tiene 
        urlArticle=a['href']
        print(urlArticle)
        #y aqui extraemos un encabezado por si lo necesitaban 
        article=pageBeauti.find('p',class_='article-item-lead')
        return urlArticle
        

    def getNoticeps5(self):
        page=requests.get(self.urlps5)
        pageBeauti=BeautifulSoup(page.content,'html.parser') 
        #extraemos el titulo por si lo necesitaban 
        title=pageBeauti.find('article',class_='card REVIEW p1')
        a=title.find('a')
        #del mismo a se extrae el url el url es lo que quieren 
        #no se une con el otro link porque ya lo tiene 
        urlArticle=a['href']
        
        #y aqui extraemos un encabezado por si lo necesitaban 
        article=pageBeauti.find('p',class_='article-item-lead')
        return urlArticle


