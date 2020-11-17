
class Admin(object):
    def __init__(self):
        #aqui tenemos los datos del admin que va a prender y apagar el bot

        self.name='!                       Izhan.l8'
        self.discriminator='0617'
        self.on=False

    def getName(self):
        return self.name

    def getDiscriminator(self):
        return self.discriminator

    def getONoff(self):
        return self.on

    def setOnoff(self):
        self.on = not self.on


