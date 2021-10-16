import pandas as pd

class Excel():
    """Создаём класс для работы с входящими данными Excel"""

    def __init__(self):
        self.table = 'excel/test_cam.xlsx'
        self.elements = pd.read_excel(self.table)
    def print_element(self):
        """Просмотр таблицы"""
        print(elements)
    
    def check_type(self):
        """Обработка типа камер"""
        list_ip = self.elements['ip'].tolist()
        print(list_ip)
        # Далее можемобрабатывать ip из list,
        # например прогнать через request и вытянуть
        # тип камеры + записать обратно


