from excel_handler import *

file = Excel()
log = open('log.txt', 'w')

# Пингуем список
file.ping_ip()
print(file.false_ping_list)

# Записываем не запинговавшиеся ip
for ip in file.false_ping_list:
    log.write(ip + ' не ответил \n')
log.close()