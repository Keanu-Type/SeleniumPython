import time
from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import csv


Translate = Translator() #Need for Translation later
switchs = bool(True)     #Need for looping later
datetoday = date.today() #Need for Date later
Header = ['LINK','NAME', 'DATE', 'PROGRESS'] #for file header

Divisible = int(0)
#CHECK IF FILE/CSV ALREADY EXIST
try:                                                         #if file not yet made, make one
    with open("NEW_Units_Alchemist_Code.csv",'x', newline='') as csvfile: #Open("Filetobecreated.csv",'x', newline='') x is need it means create file
       writer = csv.DictWriter(csvfile,fieldnames=Header)               #The Header variable in line 13 will be use here. it will be the Column Name
       writer.writeheader()                                             #Insert the header
    csvfile.close()                                                     #Close the File to save resources
except:                                                     #if already exist, skip
    time.sleep(0.1)                                             

driver = webdriver.Chrome()                         #to access chromedrivers. See README.md
driver.get("https://www.alchemistcodedb.com/units") #go to this website.    
driver.implicitly_wait(5)                           #wait 5 seconds before doing anything.

#TRANSLATING JAPANESE TO ENGLISH(Power by Google Translate)
def ConverEnglish(name): #For some reason CSV cannot accept non UTF-8 Characters like Japanese words. so we will conver it to English ascii
    if (name.isascii()): #if English/Ascii is UTF-8. do nothing
        return name
    else:                #if not English/Ascii UTF-8, Conver to English
        name=Translate.translate(name,dst='en')  #Variable.translate("Word here", dst='what language you want to translate it')
        return (name.text)


#Main Work of the code
while switchs:  #Until there is "NEXT >", The code will continue looping
    try:
        Body=[] #Dictionary for compiling all data in the current page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Scroll Down
        
        #GET THE LINK AND PRINT THE LINK
        row = driver.find_elements(By.XPATH, "./html/body/div/div/div[2]/div/div[3]/table/tbody/tr")#Find the Row where the Units/Memento are
        
        #INDIVIDUALLY TAKE ALL DATA base on the row data
        for each_unit in row: 
            Partial_Link = each_unit.find_element(By.TAG_NAME, 'a').get_attribute('href') #Link-of-the-Unit #GET LINK
            Partial_Name = each_unit.find_element(By.TAG_NAME, 'a').text                  #Name-of-the-Unit #GET NAME
            Partial_Name = ConverEnglish(Partial_Name)                                    #CHECK IF ENGLISH. IF NOT CONVERT TO ENGLISH
            Body.append({'LINK': Partial_Link, 'NAME':Partial_Name,'DATE':(datetoday.strftime("%b-%d-%Y")),'PROGRESS':"NOT_SCRAPE"}) #Date when i scrapped it

            print(Partial_Name , end="  ") #for output only. feel free to delete
            print(Partial_Link)            
            
        #INSERT ALL ITEMS IN THE CSV FILE
        with open("NEW_Units_Alchemist_Code.csv",'a', newline='') as csvfile: #open("filename.csv", 'a', newline='')
            writer = csv.DictWriter(csvfile,fieldnames=Header)              #base on the syntax on Body.append above, it will respectively put the data on the column
            writer.writerows(Body)                                          #Write all Data at once

        #GO TO NEXT PAGE
        time.sleep(2)
        page=driver.find_element(By.PARTIAL_LINK_TEXT, "Next ›") #Find the "Next > Button and page.click() or Click it"
        page.click()
        time.sleep(3)
    except:
        #IF ON LAST PAGE
        csvfile.close() #Close the File
        switchs = False #End the Loop


