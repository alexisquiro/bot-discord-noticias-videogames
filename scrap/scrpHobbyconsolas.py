
from bs4 import BeautifulSoup 
from selenium import webdriver
import requests

#lo ultimo 
class ScrpHobbyconsolas(object):
    
    def __init__ (self):
        self.url='https://www.hobbyconsolas.com/ultimo'
    
    def getNotice(self):
        try:
            page=requests.get(self.url)
            pageBeauti=BeautifulSoup(page.content,'html.parser') 
            #extraemos el titulo por si lo necesitaban 
            title=pageBeauti.find('h2',class_='article-item-title')
            a=title.next
            #del mismo a se extrae el url el url es lo que quieren 
            #se une con el otro link ya que no lo trae directamente 
            url=a['href']
            urlArticle= 'https://www.hobbyconsolas.com' +url
            #y aqui extraemos un encabezado por si lo necesitaban 
            article=pageBeauti.find('p',class_='article-item-lead')
            return urlArticle
        except:
            print('error en Hobby consola')
            return 'error en hobby consola'

        



