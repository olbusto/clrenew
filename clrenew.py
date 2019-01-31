import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/path/to/chromedriver'") # include path to chromedriver

browser.get('https://accounts.craigslist.org/login')

email = browser.find_element_by_id("inputEmailHandle")
password = browser.find_element_by_id("inputPassword")

email.send_keys("example@example.com") # login email address
password.send_keys("example") # password

browser.find_element_by_id("login").click()

renewals_done = 0

selectLinkOpeninNewTab = (Keys.COMMAND + Keys.ENTER);

renewLink = browser.find_elements_by_xpath("//input[@name='go' and @value='renew']")

if not renewLink:
    print("Nothing to renew")
if renewLink:
    print("Total renewals available: " +str(len(renewLink)))
    time.sleep(2) # 2 second delay after logging in before renewing ads

for x in range(0,len(renewLink)):
    if renewLink[x].is_displayed():
        renewLink[x].send_keys(selectLinkOpeninNewTab)
        time.sleep(1) # 1 second delay between clicking renew
        renewals_done += 1
        print("Listing renewed!")

print("Total renewals completed: "+str(renewals_done))

if renewLink:
    print("Total renewals completed: "+str(renewals_done))
    time.sleep(3) # 3 second delay after renewing ads before closing the browser

browser.quit() # close the instance of the browser.
