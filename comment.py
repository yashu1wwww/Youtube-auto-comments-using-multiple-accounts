import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','sub to your channel','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #replace with your words

email = 'virat@123@gmail.com\n'   #replace with your mail         
password = 'pass123$%\n'           #replace with your password     

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,5)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
time.sleep(2)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(2)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
time.sleep(5)

driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

time.sleep(3)

driver.execute_script("window.scrollTo(0, 600);")

time.sleep(1)

#1st acc

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 40: #Change the number 40 to however many comments you desire...
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(3)

driver.close()

#2nd acc

email = 'virat@1273@gmail.com\n'   #replace with your mail         
password = 'pass1243$%\n'           #replace with your password     

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,5)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
#time.sleep(2)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(2)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
time.sleep(5)

driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

time.sleep(3)

driver.execute_script("window.scrollTo(0, 600);")

time.sleep(1)

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 40: #Change the number 40 to however many comments you desire...
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(3)

driver.close()

#i added two accounts if you want more means copy line from 73 to 126 and paste it in 128 line and dont forgot to replace mail and password...




