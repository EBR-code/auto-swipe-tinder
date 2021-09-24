from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import random

chrome_driver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL = "https://tinder.com/"
driver.get(URL)
TINDER_MAIL = "Your_email@email.com"
TINDER_PASS = "Yourtinderpass"

# Opens tinder page to log in
time.sleep(2)
login_button = driver.find_element_by_xpath(
    '//*[@id="q633216204"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(2)
login_fb_button = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_fb_button.click()
base_window = driver.window_handles[0]
print(driver.window_handles)
time.sleep(random.randint(1, 3))

# Switches to the facebook popup window.
fb_popup_window = driver.window_handles[1]
driver.switch_to.window(fb_popup_window)
print(driver.title)

# Fill up facebook login form then logs in
time.sleep(random.randint(1, 3))
email_login_bar = driver.find_element_by_xpath('//*[@id="email"]')
email_login_bar.send_keys(TINDER_MAIL)
time.sleep(random.randint(1, 3))
password_login_bar = driver.find_element_by_xpath('//*[@id="pass"]')
password_login_bar.send_keys(TINDER_PASS)
time.sleep(random.randint(1, 3))
fb_login_button = driver.find_element_by_xpath('//*[@id="loginbutton"]')
fb_login_button.click()

# Return back to tinder
driver.switch_to.window(base_window)
print(driver.title)

# Close tinder pop-ups like accept cookies, accept location, not accept notification.
time.sleep(5)
accept_cookie_button = driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[2]/div/div/div[1]/button')
accept_cookie_button.click()
time.sleep(2)
accept_location_button = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[1]')
accept_location_button.click()
time.sleep(2)
not_accept_notification_button = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[2]')
not_accept_notification_button.click()
time.sleep(3)

# Tinder auto swipe
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(3)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="q633216204"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button ')
        like_button.click()


    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector('//*[@id="q963587405"]/div/div/div[1]/div/div[4]/button')
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()