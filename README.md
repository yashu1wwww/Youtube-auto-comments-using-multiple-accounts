# Youtube-auto-comments-using-multi-accounts
Youtube auto comments using multi accounts using selenium with python

๐๐๐๐ญ๐๐ซ ๐๐ฐ๐จ ๐จ๐ซ ๐ฆ๐จ๐ซ๐ ๐๐จ๐ฆ๐ฉ๐ข๐ฅ๐ ๐จ๐ ๐๐จ๐ญ๐ฌ ๐๐๐ญ๐๐ก ๐๐ก๐๐ฌ๐ ๐๐ข๐๐๐จ ๐๐ง๐ ๐๐จ๐ง๐ง๐๐๐ญ ๐๐ฉ๐ง ๐๐ง๐ ๐ซ๐ฎ๐ง

https://youtu.be/c9MAJpax5R0

#Replace Email and Pass in 14th & 15th line and also in 509 and 510 line 

note:-use accounts which dont have 2-factor authentication...

change url in url.txt file which url you required and change the cmt text if you needed to your required cmts in 11th line...

After download the folder extract it and open cmd and enter Python If You Find Python Version

Then enter pip install undetected_chromedriver in cmd and hit enter button (internet connection will be in on)

and enter pip install random in cmd and hit enter button

and Pip install Proxy in cmd and hit enter button

After download the chromedriver(https://chromedriver.chromium.org/downloads extract these to downloaded folder)and with matches your chrome version of your pc and

enter comment.py in cmd on that particular folder or double click on comment.py.... 

๐ YouTube Auto Cmts Using Python https://youtu.be/JJmyzyBl5bE

(these video only cmts using one acc muliple accs means after one acc cmts complete its close the tab and open the new tab and do the same process)

๐Python Install Setup=https://youtu.be/4bUOrMj88Pc

๐Note:-

๐if your selenium version is in latest version then 
the code never run 

๐open cmd and enter pip uninstall selenium

And enter 

pip install selenium==4.2.1
or
pip install selenium==4.2.0

and hit enter 

and 

python -c "import selenium; print(selenium.__version__)"
<to check the current version of selenium>


๐๐๐๐จ ๐๐ฃ๐๐ค๐ง๐ข๐๐ฉ๐๐ค๐ฃ ๐๐จ ๐ค๐ฃ๐ก๐ฎ ๐๐ค๐ง ๐๐๐ช๐๐๐ฉ๐๐ค๐ฃal ๐ฅ๐ช๐ง๐ฅ๐ค๐จ๐ ๐๐ฃ๐ ๐ฌ๐ ๐๐ง๐ ๐ฃ๐ค๐ฉ ๐ง๐๐จ๐ฅ๐ค๐ฃ๐จ๐๐๐ก๐ ๐๐ค๐ง ๐๐ฃ๐ฎ ๐?๐๐ฃ๐ ๐ค๐ ๐๐ก๐ก๐๐๐๐ก ๐๐๐ฉ๐๐ซ๐๐ฉ๐ฎ ๐๐ค๐ฃ๐ ๐๐ฎ ๐ฉ๐๐๐จ ๐ฉ๐ค๐ค๐ก.

if you cmt on your brand acc also means below is the code make separate py file for each brand acc below is the code....

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
#time.sleep(2)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(11) #if click on brand acc 2 changes to 11 or 12,13

if click on 1st brand account

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/tp-yt-paper-item-body/yt-formatted-string[1]').click()

if click on 2nd brand account

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/tp-yt-paper-item-body/yt-formatted-string[1]').click()

if click on 3rd brand account

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/tp-yt-paper-item-body/yt-formatted-string[1]').click()

if click on 4th brand account

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item/tp-yt-paper-item-body/yt-formatted-string[1]').click()

if click on 5th brand account

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item/tp-yt-paper-item-body/yt-formatted-string[1]').click()

if click on 6th brand account

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item/tp-yt-paper-item-body/yt-formatted-string[1]').click()

if click on 7th brand account

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item/tp-yt-paper-item-body/yt-formatted-string[1]').click()

if click on 8th brand account

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-channel-switcher-renderer/div[2]/div/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item/tp-yt-paper-item-body/yt-formatted-string[1]').click()

time.sleep(3)
