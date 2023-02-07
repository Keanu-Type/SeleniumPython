import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import csv
#os.environ['PATH']+= r"C:/SeleniumDrivers"
f = open("Alchemist_Code.csv", "w")
Header=['Link','Name','Last Date']
driver = webdriver.Chrome() #to access chromedrivers
datetoday = date.today()
driver.get("https://www.alchemistcodedb.com/units") #go to this website
driver.implicitly_wait(5) #wait 30 seconds.

x = int(10)
i = int(0)
switchs = bool(True)
while switchs:

    try:
        #GET THE LINK AND PRINT THE LINK
            #units = driver.find_elements(By.CLASS_NAME, "clickable")
        row = driver.find_elements(By.XPATH, "./html/body/div/div/div[2]/div/div[3]/table/tbody/tr")
        for each_unit in row:
            Partial_Link = each_unit.find_element(By.TAG_NAME, 'a').get_attribute('href')   
            Partial_Name = each_unit.find_element(By.TAG_NAME, 'a').text
            #nameB = nameA.find_element(By.XPATH, './/div[2]').get_attribute('href')
            print(Partial_Name , end="  ")
            print(Partial_Link)
            print(datetoday.strftime("%b-%d-%Y"))
            Insert_Link = [Partial_Link, Partial_Name, (datetoday.strftime("%b-%d-%Y"))]

        page=driver.find_element(By.PARTIAL_LINK_TEXT, "Next")#CLICK NEXT PAGE
        
        page.click()
        time.sleep(3)
        print("----NEXT PAGE-----")
    except:
        switchs = False


