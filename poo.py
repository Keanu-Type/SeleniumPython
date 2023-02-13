import time
import csv
from urllib.request import Request, urlopen
import urllib
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.window import WindowTypes
import urllib.request
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
from selenium.webdriver.support.ui import Select
# I remove global driver because you cannot use shared driver in multiprocess.

from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#def test_func(link):
#    driver.switch_to.new_window(WindowTypes.TAB)
#    driver.get(link)
driver.get("https://cdn.alchemistcodedb.com/file/bb-acdb/images/UnitImages/awake_emme.png")
link=driver.get("https://cdn.alchemistcodedb.com/file/bb-acdb/images/UnitImages/awake_emme.png") #Open Links individually
#src = driver.find_element(By.XPATH, "/html/body/img").get_attribute('src')
#urllib.request.urlretrieve(src,"Image_Test.png")

#driver.get(url)

    # get the image source
Target_Image = driver.find_element(By.XPATH, "/html/body/img")

src = []

src.append(Target_Image.get_attribute('src'))
# Retrieve and download the images.
actionChains = ActionChains(driver)
cmd_ctrl = Keys.CONTROL
#ActionChains(driver).key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL).perform()
#time.sleep(5)
actionChains.move_to_element(Target_Image).context_click()
time.sleep(1)
actionChains.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(1)
actionChains.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(1)

#with open('Logo.png', 'wb') as file:
#identify image to be captured
#   l = driver.find_element(By.XPATH, '/html/body/img')
#write file
#   file.write(l.screenshot_as_png)
#   time.sleep(3)
#close browser
#driver.quit()
#script_js = 'var dataURL = document.getElementsByClassName("_cx6")[0].toDataURL("image/png");' \

#actionChains = ActionChains(driver)
#actionChains.move_to_element(img).context_click()
#time.sleep(0.5)
#actionChains.send_keys(Keys.ARROW_DOWN).perform()
#time.sleep(0.5)
#actionChains.send_keys(Keys.ARROW_DOWN).perform()
#time.sleep(0.5)
