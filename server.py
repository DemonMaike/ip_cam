import requests
from requests.exceptions import ConnectTimeout
from excel_handler import Excel
import datetime
import os

# С ping могут быть проблемы в разных OS, лучше сразу запрос и по ответу от сервера все понятно
class Server:
    def __init__(self):
        self.DB = Excel()
        self.log = "error.log"
        self.proto_schema = "http://"
        self.folderImages = "images"
        if (not os.path.exists):
            os.mkdir(self.folderImages, mode=0o644)
            self.log("Create {} dir".format(self.folderImages))
        
    def cam_test(self):
        for ip in self.DB.list_ip:
            try:
                port = ''
                r = requests.get(self.proto_schema + ip + port + '/', timeout = 10)
                print(r.status_code)
            except ConnectTimeout as e:
                self.logger("Camera from {}{} not avalibale".format(ip, port))
            except Exception as e:
                print(e)

    def logger(self, msg):
        log = {'timestamp': datetime.datetime.now(), 'msg': msg}
        with open(self.log, 'a') as f:
            f.write("{timestamp}: {msg}\n".format(**log))
    
    #Метод получения кратинки по ссылке
    def get_picture(self):
        pass

    def save_picture(self, id, image):
        name = "{}_{}.png".format(datetime.datetime.now(), id)
        with open(name, "wb") as f:
            f.write(image)
        

if __name__ == "__main__":
    s = Server()
    s.cam_test()