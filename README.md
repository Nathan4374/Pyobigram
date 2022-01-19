# pyobigram
api sencilla para la creacion de bots de telegram , actualmente v0.1 , la estara actualizando aqui en mi github.

# Ejemplo Pyton

    $ python3
    from pyobigram.utils import sizeof_fmt,downloadProgressFile
    from pyobigram.client import ObigramClient
    
    def onmessage(update,bot:ObigramClient):
    message = bot.sendMessage(update.message.chat.id,'Procesando...')
    
    if __name__ == '__main__':
        bot = ObigramClient('5073400824:AAH3DYCJKxV2FkZpprnbBel0TUb-L0ib2DE')
        bot.onMessage(onmessage)
        bot.run()
    >>>



# Contactame
Telegram : https://t.me/obisoftdev
Whatsapp : +5354858181
