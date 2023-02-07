import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import csv

switchs = bool(True)
datetoday = date.today()
Header = ['LINK','NAME', 'DATE'] #for file header
#CHECK IF FILE EXIST
try: #if file not yet made, make one
    with open("Alchemist_Code.csv",'x', newline='') as csvfile:
       writer = csv.DictWriter(csvfile,fieldnames=Header)
       writer.writeheader() 
    csvfile.close()
except: #if already exist, skip
    time.sleep(0.1)

driver = webdriver.Chrome() #to access chromedrivers
driver.get("https://www.alchemistcodedb.com/units") #go to this website
driver.implicitly_wait(5) #wait 5 seconds.

#Main work
while switchs:
    try:
        Body=[]
        #GET THE LINK AND PRINT THE LINK
        row = driver.find_elements(By.XPATH, "./html/body/div/div/div[2]/div/div[3]/table/tbody/tr")#FIND THE ROW AND COUNT HOW MANY
        for each_unit in row: #INDIVIDUALLY TAKE ALL DATA
            Partial_Link = each_unit.find_element(By.TAG_NAME, 'a').get_attribute('href') #Link-of-the-Unit #GET LINK
            Partial_Name = each_unit.find_element(By.TAG_NAME, 'a').text                  #Name-of-the-Unit #GET NAME
            Body.append({'LINK': Partial_Link, 'NAME':Partial_Name,'DATE':(datetoday.strftime("%b-%d-%Y"))}) #Date when i scrapped it

            print(Partial_Name , end="  ") #for output only. feel free to delete
            print(Partial_Link)            
            
        #INSERT ALL ITEMS IN THE CSV FILE
        with open("Alchemist_Code.csv",'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=Header)
            writer.writerows(Body) #Write all Data at once

        #NEXT PAGE
        page=driver.find_element(By.PARTIAL_LINK_TEXT, "Next")
        page.click()
        time.sleep(3)
    except:
        #IF ON LAST PAGE
        csvfile.close()
        switchs = False


