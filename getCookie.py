from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time, json, pickle
import keyboard


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

#-------------获取cookies-------------------------------------#
# 打开淘宝登录页面
login_url = "https://loginmyseller.taobao.com/?from=taobaoindex&f=top&style=&sub=true&redirect_url=https%3A%2F%2Fmyseller.taobao.com%2F%3Fspm%3Da21dvs.24173238.0.0.26381544n6jXPQ"
driver.get(login_url)
time.sleep(3)
time.sleep(60)

cookies = driver.get_cookies()
print(type(cookies))
cookiesFile = json.dumps(cookies)
print(type(cookiesFile))

with open('cookiesFile.json','w') as myfile:
    myfile.write(cookiesFile)


#---------------------------------------------#
# driver.delete_all_cookies()

# with open('cookiesFile.json','r') as file1:
#     cookiesInfo = json.loads(file1.read())
#     print(cookiesInfo)
# for i in range(0, len(cookiesInfo)):
#     if isinstance(cookiesInfo[i].get('expiry'),float):
#         cookiesInfo[i]['expiry'] = int(cookiesInfo[i]['expiry'])
#     driver.add_cookie(cookiesInfo[i])
#     print(cookiesInfo[i])

# driver.refresh()

# time.sleep(3)