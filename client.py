import requests
import json
import threading
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace
import time
import codecs


class ObigramClient(object):
    def __init__(self,token):
        self.token = token
        self.path = 'https://api.telegram.org/bot' + token + '/'
        self.files_path = 'https://api.telegram.org/file/bot' + token + '/'
        self.runing = False
        self.funcs = {}
        self.update_id = 0
        self.onmessage = None

        self.SendFileTypes = {'document':'SendDocument','video':'SendVideo'}


    def startNewThred(self,targetfunc=None,args=()):
        processThread = threading.Thread(target=targetfunc, args=args);
        processThread.start();
        pass

    def run(self):
        self.runing = True
        while self.runing:
            try:
                getUpdateUrl = self.path + 'getUpdates?offset=' + str(self.update_id+1)
                update = requests.get(getUpdateUrl)

                updates = json.loads(update.text, object_hook = lambda d : Namespace(**d)).result

                if len(updates) > 0:
                    self.update_id = updates[-1].update_id

                try:
                    for func in self.funcs:
                        for update in updates:
                                if func in update.message.text:
                                    self.startNewThred(self.funcs[func],(update,self))
                except:pass

                try:
                    if self.onmessage:
                        for update in updates:
                            self.startNewThred(self.onmessage,(update,self))
                except:pass

            except Exception as ex:
                self.runing = False
            pass
        pass

    def sendMessage(self,chat_id=0,text=''):
        sendMessageUrl = self.path + 'sendMessage?chat_id=' + str(chat_id) + '&text=' + text
        result = requests.get(sendMessageUrl).text
        return json.loads(result, object_hook = lambda d : Namespace(**d)).result

    def editMessageText(self,message,text=''):
        editMessageUrl = self.path+'editMessageText?chat_id='+str(message.chat.id)+'&message_id='+str(message.message_id)+'&text=' + text
        result = requests.get(editMessageUrl).text
        return json.loads(result, object_hook = lambda d : Namespace(**d)).result
    
    def sendFile(self,chat_id,file,type='document'):
        sendDocumentUrl = self.path + self.SendFileTypes[type]
        of = codecs.open(file)
        payload_files = {type:(file,of)}
        payload_data = {'chat_id':chat_id}
        result = requests.post(sendDocumentUrl,files=payload_files,data=payload_data).text
        of.close()
        parse = json.loads(result, object_hook = lambda d : Namespace(**d))
        return parse.result

    def getFile(self,file_id):
        getFileUrl = self.path + 'getFile?file_id=' + str(file_id)
        result = requests.get(getFileUrl).text
        parse = json.loads(result, object_hook = lambda d : Namespace(**d)).result
        return parse

    def downloadFile(self,file_id=0,destname='',progressfunc=None,args=None):
        reqFile = self.getFile(file_id)
        downloadUrl = self.files_path + str(reqFile.file_path)
        req = requests.get(downloadUrl, stream = True,allow_redirects=True)
        if req.status_code == 200:
            file_wr = open(destname,'wb')
            chunk_por = 0
            chunkrandom = 100
            total = reqFile.file_size
            time_start = time.time()
            time_total = 0
            size_per_second = 0
            for chunk in req.iter_content(chunk_size = 1024):
                    chunk_por += len(chunk)
                    size_per_second+=len(chunk);
                    tcurrent = time.time() - time_start
                    time_total += tcurrent
                    time_start = time.time()
                    file_wr.write(chunk)
                    if time_total>=1:
                        if progressfunc:
                            progressfunc(destname,chunk_por,total,size_per_second,args)
                        time_total = 0
                        size_per_second = 0
            file_wr.close()
        return destname

    def on (self,name,func):self.funcs[name] = func
    def onMessage (self,func):self.onmessage = func

