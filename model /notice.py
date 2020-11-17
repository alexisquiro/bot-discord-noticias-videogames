#esta clase era de opcional

class Notice(object):
    def __init__(self,url,image,article):
        self.url = url
        self.image = image 
        self.title=''
        self.article = article 
    
    def getImage(self):
        return self.image 
    
    def getUrl(self):
        return self.url 
    
    def getArticle(self):
        return self.article 

