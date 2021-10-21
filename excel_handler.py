import pandas as pd
import os
class Excel():
#Создаём класс для работы с входными данными Excel
    def __init__(self):
        self.table = 'excel/test_cam.xlsx'
        self.elements = pd.read_excel(self.table)
        self.list_ip = self.elements['ip'].tolist()
        self.false_ping_list = []

    def print_table(self):
        """Просмотр таблицы"""
        print(self.elements)

    def ping_ip(self):
        """ прогоняем через пинг все ip адреса"""
        for i in self.list_ip:
            ping = os.system('ping ' + i)
            print(ping)
            if ping == 0:
                pass  # добавим цикл
            # для подстановки ссылок и запись
            # подходящей ссылки, если есть подходящая,
            # запись типа, если нет - пишем в лог для этого
            # ip нет подходящей ссылки
            else:
                self.false_ping_list.append(i)