# pyobigram v1.6
api sencilla para la creacion de bots de telegram , la estara actualizando aqui en mi github.

# Ejemplo Base (Pyton)

    $ python 3
    from pyobigram.client import ObigramClient
    
    def onmessage(update,bot:ObigramClient):
    message = bot.sendMessage(update.message.chat.id,'Procesando...')
    
    if __name__ == '__main__':
        bot = ObigramClient('BOT TOKEN')
        bot.onMessage(onmessage)
        bot.run()

# actualizaciones
    debuelbe un objeto message : bot.sendMessage(chat_id,text,parse_mode) : envia un mensage
    debuelbe un objeto message : bot.editMessageText(message,text,parse_mode) : edita un mensaje
    debuelbe un objeto file : bot.sendFile(chat_id,file,type) : envia un archivo
    debuelbe un objeto fileinfo : bot.getFile(file_id) : extrae informacion de ese archivo
    debuelbe un str ruta : bot.downloadFile(file_id=0,destname='',progressfunc=None,args=None) : descarga un archivo 
    debuelbe un bolean : bot.answerInline(inline_query_id=0,result=[]) : responder al modo inline
    bot.on(cmd_hanlde) : inicia la escucha de un comando , loas parametros del handle son (update,bot)
    bot.onMessage(message_handle) : inicia la escucha de una actualizacion completa , loas parametros del handle son (update,bot)
    bot.onInline(inline_handle) : inicia la escucha en el modo inline , loas parametros del handle son (update,bot)

# funciones
     from pyobigram.client import inlineQueryResultArticle
     inlineQueryResultArticle() : crear un objeto articulo para respuesta al modo inline

# Contactame
Telegram : https://t.me/obisoftdev
Whatsapp : +5354858181
