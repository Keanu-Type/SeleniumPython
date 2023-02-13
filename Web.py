import csv
import urllib
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.window import WindowTypes
import urllib.request


driver = webdriver.Chrome()  
with open("Units_Alchemist_Code.csv", "r+", newline='') as csv_file:
    outlines = []
    for unit in csv.reader(csv_file):
        #print(*unit[0:1])

        links=[]
        if unit[-1] == "NOT_SCRAPE":
            link=str(*unit[0:1]) #remove the []. without *. the output is "[LINK]" instead of "LINK"
            link+= "#profile"
            print(link)
            driver.get(link) #go to this website. 

            wait=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
            try:
                body = driver.find_element(By.ID, "profile")
                image_set = body.find_elements(By.XPATH, './div/div[2]/div[2]/div')
                for image in image_set:
                    links.append(image.find_element(By.TAG_NAME, 'a').get_attribute('href'))
                    
                    
                
                for open_links in links:
                    driver.switch_to.new_window(WindowTypes.TAB)
                    driver.get(open_links) #Open Links individually
                    src = driver.find_element(By.XPATH, "/html/body/img").get_attribute('src')
                    urllib.request.urlretrieve(src,"Image_Test.png")

            except:
                print("none")
              #  break
            #image_set = driver.find_elements(By.CLASS_NAME, "Card")
            #print(image_set)
            #for each_image in image_set:
            #    Image_Link = each_image.find_element(By.TAG_NAME, 'a').get_attribute('href')
            #    print(Image_Link)
            #time.sleep(0.01)
            
            
            print("done")
            #break
     #   else:
     #       unit[-1] = " True"
     #   outlines.append(unit)
    #csv_file.seek(0)
    #writer = csv.writer(csv_file)
    #for line in outlines:
    #    writer.writerow(line)