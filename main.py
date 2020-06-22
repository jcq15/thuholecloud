import requests
import json
import time

u_getcmt = r'https://thuhole.com/services/thuhole/api.php?action=getcomment&pid='
u_getone = r'https://thuhole.com/services/thuhole/api.php?action=getone&pid='

for i in range(12,27):
    with open('data.txt', 'a', encoding='utf-8') as f:
        for j in range(1,101):
            f.write(requests.get(u_getone + str(i*100+j)).content.decode()+'\n')
            print(i*100+j)
            time.sleep(0.02)
