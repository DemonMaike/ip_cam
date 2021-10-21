import pandas as pd
import os
class Excel():
    """Создаём класс для работы с входными данными Excel"""

    def __init__(self):
        self.table = 'excel/test_cam.xlsx'
        self.elements = pd.read_excel(self.table)
        self.list_ip = self.elements['ip камер'].tolist()
        #self.list_type = self.elements['Тип камер'].tolist()
        self.links_photo = self.elements['Ссылки для снятия скриншотов'].tolist()
        self.false_ping_list = []

    def print_table(self):
        """Просмотр таблицы"""
        print(self.elements)

    def ping_ip(self):
        """ прогоняем через пинг все ip адреса"""
        for ip in self.list_ip:
            ping = os.system('ping ' + ip)
            print(ping)
            if ping == 0:
                pass  # добавим цикл
            # для подстановки ссылок и запись
            # подходящей ссылки, если есть подходящая,
            # запись типа
            else:
                self.false_ping_list.append(ip)
    
 #   def _type_cam(self):
  #      for link in self.links_photo:

