# pyobigram
api sencilla para la creacion de bots de telegram , actualmente v0.1 , la estara actualizando aqui en mi github.

# Ejemplo Pyton
def onmessage(update,bot:ObigramClient):
    message = bot.sendMessage(update.message.chat.id,'Procesando...')
def onCD(update,bot:ObigramClient):
    import os
    files = os.listdir(os.path.abspath(''))
    reply_text = 'Archivos:\n'
    for f in files:
        size = sizeof_fmt(os.stat(f).st_size)
        reply_text += f + ' - ' + size + '\n'
    bot.sendMessage(update.message.chat.id,reply_text)
if __name__ == '__main__':
    bot = ObigramClient('5073400824:AAH3DYCJKxV2FkZpprnbBel0TUb-L0ib2DE')
    bot.onMessage(onmessage)
    bot.run()

# Contactame
Telegram : https://t.me/obisoftdev
Whatsapp : +5354858181
