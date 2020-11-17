
import discord
from discord.ext import commands,tasks
from scrap.scrpHobbyconsolas import ScrpHobbyconsolas
from scrap.scrpPuregamming import ScrpPuregamming
from scrap.scrpIgnesp import ScrpIgnesp
import time
import datetime
from keep_alive import keep_alive
from threading import Thread
from flask import Flask
import random
#puse esta clase aqui porque mi pc no agarra la carpeta model


class Admin(object):
    def __init__(self):
        #aqui tenemos los datos del admin que va a prender y apagar el bot
        self.name = '!                       Izhan.l8'
        self.discriminator = '0617'
        self.on = True
        self.ctx = ''
        self.now=datetime.datetime.now()
        self.end=self.now + datetime.timedelta(minutes=5)
	
    def getName(self):
        return self.name

    def getDiscriminator(self):
        return self.discriminator
    

    def getONoff(self):
        return self.on

    def getCtx(self):
        return self.ctx

    def getNow(self):
        return self.now

    def getEnd(self):
        return self.end

    def setNow(self,now):
        self.now=now
    
    def setEnd(self,end):
        self.end=end

    def setCtx(self, ctx):
        self.ctx = ctx

    def setOnoff(self):
        #se cambia de True a false para que este activo o no
        self.on = not self.on

    def auth(self, ctx):
        #se verifica que este en el cana notice y sea el admin qu eactive el bot
        #si el canal de discord cambia solo cambia el canal 'notice' por el nuevo nombre
        if ctx.channel.name == 'notice' and self.name == ctx.author.name and self.discriminator == ctx.author.discriminator:
            return True
        else:
            return False








app = Flask('')


#se instancia el admin
admin = Admin()

#se instancian los scrapping
pureg = ScrpPuregamming()
hobby = ScrpHobbyconsolas()
ign = ScrpIgnesp()
#se intancia Disccord
client = discord.Client()
bot = commands.Bot(command_prefix='!', description='Bot de noticias ')


#comandos secundarios que activa el comando principal no ejecutar
@bot.command(name='url3')
async def url3(ctx):
	if admin.auth(ctx):
		print('url')
		ignurl = ign.getNoticeps5()
		await ctx.channel.send(ignurl)
	else:
		print('ign')


#comandos secundarios que activa el comando principal no ejecutar
@bot.command(name='url2')
async def url2(ctx):
	if admin.auth(ctx):
		print('url')
		ignurl = ign.getNoticexbox()
		await ctx.channel.send(ignurl)
	else:
		print('entor en xbox')


#comandos secundarios que activa el comando principal no ejecutar
@bot.command(name='url1')
async def url1(ctx):
	if admin.auth(ctx):
		print('url')
		hobbyurl = hobby.getNotice()
		await ctx.channel.send(hobbyurl)
	else:
		print('hobby')





#aqui puedes cambiar las horas 
@tasks.loop(hours=8)
async def sendHello():
    now=datetime.datetime.now()
    print(now)
    ctx =admin.getCtx()
    await ctx.channel.send('sendHello')
    await url1(ctx)
    #este time es para que no envie las noticias todas juntas
    time.sleep(5)
    await url2(ctx)
    #igual este
    time.sleep(10)
    await url3(ctx)
    #igual este
    time.sleep(12)
    pureUrl = pureg.getNotice()
    await ctx.channel.send(pureUrl)
    #este time es para cada 8 horas se envien las noticias lo pueden modificar
    




#comando principal que activa el bot
@bot.command(name='url')
async def url(ctx):
    pass
		





@bot.event
async def on_ready():

    print(bot.guilds)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



@bot.event
async def on_message(ctx):
    if admin.auth(ctx) and admin.getONoff() :
        #aqui se espera que el admin ingrese un mensaje desde el canal que se quiere 
        #y se cierra para que no haya interferencia esto se ejecuta una vez si quiere que pare hay que apagarlo 
        admin.setOnoff()
        sendHello.start()
        admin.setCtx(ctx)
        print(ctx)

    





@app.route('/')
def home():
    #cada 5 minutos cuando haga ping se actualizara la hora now
    now = datetime.datetime.now()


    print(now)
    return 'hey!'



def run():
    app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)




def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()
	
	
keep_alive()


#aqui va el token

bot.run('Nzc2MTQxNzA3NTQ4Njg4Mzk0.X6wkSw.xmH9NLGp0YBoTWGfygAOLwMXfMI')
