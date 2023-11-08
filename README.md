# Youtube-auto-comments-using-multi-accounts
Youtube auto comments using multi accounts using selenium with python

👉𝐀𝐟𝐭𝐞𝐫 𝐓𝐰𝐨 𝐨𝐫 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐩𝐢𝐥𝐞 𝐨𝐟 𝐛𝐨𝐭𝐬 𝐖𝐚𝐭𝐜𝐡 𝐓𝐡𝐞𝐬𝐞 𝐕𝐢𝐝𝐞𝐨 𝐀𝐧𝐝 𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐕𝐩𝐧 𝐚𝐧𝐝 𝐫𝐮𝐧

https://youtu.be/c9MAJpax5R0

# Note: Use accounts that do not have two-factor authentication...

Change the email and password in the 14th and 15th lines, as well as in the 73 & 74th lines.

Also, change the URL in the url.txt file to the desired URL and change the comments text that you needed in the 11th line..

# Change the number 30 to how many comments you want in 60th and 117th line...

After downloading the folder, extract it and open the command prompt. If you have Python installed, type "Python" in the command prompt to check the version.

Then type "pip install undetected_chromedriver" in the command prompt and press the Enter button.

Make sure that you have an active internet connection.

Type "pip install random" in the command prompt and press the Enter button.

After downloading the chromedriver from https://chromedriver.chromium.org/downloads,

extract it to the downloaded folder that matches the version of your Chrome browser.

Type "comment.py" in the command prompt in that particular folder or double-click on comment.py


👉Python Install Setup

https://youtu.be/4bUOrMj88Pc

👉Note:-

👉if your selenium version is in latest version then 
the code never run 

👉open cmd and enter pip uninstall selenium

And enter 

pip install selenium==4.2.1
or
pip install selenium==4.2.0

and hit enter 

and 

python -c "import selenium; print(selenium.__version__)"
<to check the current version of selenium>


𝙏𝙝𝙞𝙨 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣al 𝙥𝙪𝙧𝙥𝙤𝙨𝙚 𝙖𝙣𝙙 𝙬𝙚 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙠𝙞𝙣𝙙 𝙤𝙛 𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙙𝙤𝙣𝙚 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡.

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
