# pyobigram v0.2
api sencilla para la creacion de bots de telegram , la estara actualizando aqui en mi github.

# Ejemplo Pyton

    $ python 3
    from pyobigram.client import ObigramClient
    
    def onmessage(update,bot:ObigramClient):
    message = bot.sendMessage(update.message.chat.id,'Procesando...')
    
    if __name__ == '__main__':
        bot = ObigramClient('BOT TOKEN')
        bot.onMessage(onmessage)
        bot.run()


# Contactame
Telegram : https://t.me/obisoftdev
Whatsapp : +5354858181
