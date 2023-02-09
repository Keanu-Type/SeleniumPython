import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

driver = webdriver.Chrome()  
with open("Units_Alchemist_Code.csv", "r+", newline='') as csv_file:
    outlines = []
    for unit in csv.reader(csv_file):
        #print(*unit[0:1])


        if unit[-1] == "NOT_SCRAPE":
            link=str(*unit[0:1]) #remove the []. without *. the output is "[LINK]" instead of "LINK"
            link= "https://www.alchemistcodedb.com/unit/thol"+"#profile"
            print(link)
            driver.get(link) #go to this website. 
            #driver.implicitly_wait(1)
            #rint(*unit[:2])
            #print(" ".join(unit))
            wait=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
            time.sleep(0.01)
            print("done")
            break
     #   else:
     #       unit[-1] = " True"
     #   outlines.append(unit)
    #csv_file.seek(0)
    #writer = csv.writer(csv_file)
    #for line in outlines:
    #    writer.writerow(line)