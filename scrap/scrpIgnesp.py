
from bs4 import BeautifulSoup 
from selenium import webdriver
import requests

#xbox y ps5 

class ScrpIgnesp(object):
    
    def __init__ (self):
        self.urlxbox='https://es.ign.com/xbox-series-x'
        self.urlps5='https://es.ign.com/ps5'

    def getNoticexbox(self):
        try:
            page=requests.get(self.urlxbox)
            pageBeauti=BeautifulSoup(page.content,'html.parser') 
            #extraemos el titulo por si lo necesitaban 
            thumb=pageBeauti.find('a',class_='thumb')
            #del mismo a se extrae el url el url es lo que quieren 
            #no se une con el otro link porque ya lo tiene 
            urlArticle=thumb['href']
            
            return urlArticle
        except:
            print('error en xbox')
            return 'error en xbox'
        

    def getNoticeps5(self):
        try:
            page=requests.get(self.urlps5)
            pageBeauti=BeautifulSoup(page.content,'html.parser') 
            #extraemos el titulo por si lo necesitaban 
            thumb=pageBeauti.find('a',class_='thumb')
            #del mismo a se extrae el url el url es lo que quieren 
            #no se une con el otro link porque ya lo tiene 
            urlArticle=thumb['href']
            
            return urlArticle
        except:
            print('error en ps5')
            return 'error en ps5'


