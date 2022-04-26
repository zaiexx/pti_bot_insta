from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


URL = "https://www.instagram.com/accounts/login/"
USERNAME = "victor.a.a.n"
PASSWORD = ""
ACCOUNT = "m.perezsilva"
MESSAGE = "Saludos desde python"

browser = webdriver.Chrome()
browser.get(URL)
wait = WebDriverWait(browser, 10)


sleep(3)

username = browser.find_element(By.NAME,'username')
password = browser.find_element(By.NAME,'password')

username.clear()
password.clear()

username.send_keys(USERNAME)
sleep(1)
password.send_keys(PASSWORD)

sleep(3)

browser.find_element(By.CLASS_NAME,'sqdOP.L3NKy.y3zKF').click()
sleep(3)

browser.find_element(By.CLASS_NAME,'sqdOP.yWX7d.y3zKF').click()
sleep(3)

browser.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]').click()
sleep(3)

search = browser.find_element(By.CLASS_NAME,'XTCLo.d_djL.DljaH')
search.clear()
search.send_keys(ACCOUNT)
sleep(2)

browser.find_element(By.CLASS_NAME,'-qQT3').click()
sleep(2)

photo = browser.find_element(By.CSS_SELECTOR,'.v1Nh3.kIKUG._bz0w a').get_attribute('href');
browser.get(photo)
sleep(2)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".X7cDz")))
comment = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".X7cDz textarea.PUqUI.Ypffh")))
comment.click()
sleep(2)

comment = browser.find_element(By.CLASS_NAME,'PUqUI.Ypffh')
comment = browser.find_element(By.CLASS_NAME,'PUqUI.Ypffh')
comment.send_keys(MESSAGE)
sleep(2)


browser.find_element(By.CSS_SELECTOR,'button[type=submit]').click()

#browser.find_element(By.CLASS_NAME,'sqdOP.yWX7d.y3zKF').submit()
sleep(2)
