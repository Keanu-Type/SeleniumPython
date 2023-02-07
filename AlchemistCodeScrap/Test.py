import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
#os.environ['PATH']+= r"C:/SeleniumDrivers"

driver = webdriver.Chrome() #to access chromedrivers

driver.get("https://www.alchemistcodedb.com/units") #go to this website
driver.implicitly_wait(5) #wait 30 seconds.

#WebDriverWait(driver, 30).until(
#    EC.text_to_be_present_in_element(By.CLASSNAME, 'progress-label'), "Complete!")
x = int(10)
i = int(0)
switchs = bool(True)
while switchs:

    try:
        page=driver.find_element(By.PARTIAL_LINK_TEXT, "Next")
        #ele=driver.find_Element(By.xpath(“//<tagName>[contains(text(),’textvalue’)]”))
        #page=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[4]/nav/ul")
        #Paging=page.find_element(By.)
        page.click()
        time.sleep(3)
    except:
        switchs = False
print("end")
time.sleep(30)