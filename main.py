from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import keyboard
# 设置Chrome WebDriver的路径
# driver_path = '路径/to/chromedriver'
#请求头
# Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36


custom_headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    # 'Referer': 'https://example.com',
    # 添加其他自定义字段
}
# 初始化WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Chrome(options=options)

# 打开淘宝登录页面
login_url = "https://loginmyseller.taobao.com/?from=taobaoindex&f=top&style=&sub=true&redirect_url=https%3A%2F%2Fmyseller.taobao.com%2F%3Fspm%3Da21dvs.24173238.0.0.26381544n6jXPQ"
driver.get(login_url)

# 等待登录页面加载完成
wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
# iframe = driver.find_element(By.XPATH, '//iframe[@id="alibaba-login-box"]')


element = wait.until(EC.presence_of_element_located((By.ID, 'alibaba-login-box')))

driver.switch_to.frame("alibaba-login-box")
submit_button = driver.find_element(By.CSS_SELECTOR,'.iconfont.icon-password')
time.sleep(1)
submit_button.click()


element = wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
time.sleep(1)
# 输入用户名和密码
username_input = driver.find_element(By.ID,'fm-login-id')
password_input = driver.find_element(By.ID,'fm-login-password')
username_input.click()
time.sleep(1)
username_input.send_keys('17806261557')
time.sleep(1)
password_input.click()
time.sleep(1)
password_input.send_keys('gaihuen992k')
time.sleep(1)

# try:
    # element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'nc_1_n1z')))
    # slider = driver.find_element(By.ID,'nc_1_n1z')
    # start_x = slider.location['x']
    # end_x = start_x + slider.size['width']

    # # 计算慢速滑动的间隔（可以根据需要调整）
    # slow_speed_interval = 0.1  # 0.1秒一次移动

    # # 执行慢速滑动操作
    # action = ActionChains(driver)
    # action.click_and_hold(slider)

    # # 分多次移动滑块
    # for _ in range(int(end_x / 10)):  # 10是每次移动的距离，可以根据需要调整
    #     action.move_by_offset(10, 0)  # 移动10个像素
    #     action.pause(slow_speed_interval)  # 等待一段时间，模拟慢速滑动

    # action.release().perform()
    # print("ok4")
#     pass
# except Exception as e:
#     print(f"未发现滑块验证: {e}")



# 提交登录表单
submit_button = driver.find_element(By.CSS_SELECTOR,'.fm-button.fm-submit.password-login')
submit_button.click()


try:
    # 等待登录完成
    wait.until(EC.url_changes(login_url))
except Exception as e:
    print(f"登录失败: {e}")
 
# 登录完成后可以执行其他操作，例如爬取数据




keyboard.wait("esc")
# 最后，关闭浏览器
driver.quit()