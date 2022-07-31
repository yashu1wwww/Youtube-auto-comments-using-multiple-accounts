import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'most@gmail.com\n'   #change to your mail
password = 'most@#$\n'           #change to your pass  

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(3)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  

time.sleep(5)
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

#time.sleep(3)

driver.execute_script("window.scrollTo(0, 600);")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("dboss")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("darshan")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("super")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("swamy")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("kariya")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

#time.sleep(5)

driver.close()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'error@gmail.com\n'   #change to your mail
password = 'error\n'           #change to your pass  

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(3)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  

time.sleep(5)

driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

#time.sleep(3)

driver.execute_script("window.scrollTo(0, 600);")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("dboss")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("challenging star")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("darshan")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("swamy")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("kariya")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

#time.sleep(5)

driver.close()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'elon@3@gmail.com\n'   #change to your mail
password = 'Dev@#\n'           #change to your pass  

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(3)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  

time.sleep(5)
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

#time.sleep(3)

driver.execute_script("window.scrollTo(0, 600);")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("dboss")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("challenging star")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("darshan")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("swamy")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("kariya")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

#time.sleep(5)

driver.close()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'massclass@gmail.com\n'   #change to your mail
password = 'mass#\n'           #change to your pass  

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(3)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  

time.sleep(5)
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

#time.sleep(3)

driver.execute_script("window.scrollTo(0, 600);")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("dboss")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("challenging star")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("darshan")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("swamy")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("kariya")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()
#time.sleep(5)

driver.close()

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'nameless@gmail.com\n'   #change to your mail
password = 'New123we\n'           #change to your pass  

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(3)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  

time.sleep(5)
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

#time.sleep(3)

driver.execute_script("window.scrollTo(0, 600);")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("dboss")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("challenging star")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("darshan")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("swamy")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)
    
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys("kariya")

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()
#time.sleep(5)

driver.close()

