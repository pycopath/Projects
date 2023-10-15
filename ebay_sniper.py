import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = input("Paste the url to the item: ")
max_bid = float(input("max bid is: "))
user = input("Enter username: ")
psw = input("Enter password: ")


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(url)

#Log into your account
def sign_in():
    link = driver.find_element(By.LINK_TEXT, "Sign in")
    link.click()  
    driver.implicitly_wait(60)  
    username = driver.find_element(By.ID, "userid")
    username.send_keys(user)
    driver.implicitly_wait(60)
    continue_button = driver.find_element(By.ID, "signin-continue-btn")
    continue_button.click()
    driver.implicitly_wait(60)
    password = driver.find_element(By.ID, "pass")
    password.send_keys(psw)
    sign_in_button = driver.find_element(By.ID, "sgnBt")
    sign_in_button.click()
    time.sleep(3)
sign_in()


bid_amt = driver.find_element(By.CLASS_NAME, "x-additional-info__textual-display",)
bid_amt = bid_amt.text
bid_amt = str(bid_amt)
bid_amt = bid_amt[:0] + bid_amt[10:]
bid_amt = float(bid_amt[:5])
#^^^^^^CHANGE VARIABLE FOR HIGHER PRICED ITEMS


time_left = driver.find_element(By.CLASS_NAME, "ux-timer")
time_left = time_left.text
time_left = str(time_left[:2])


bid_button = driver.find_element(By.ID, "bidBtn_btn")
bid_button.click()
driver.implicitly_wait(10)
bid_box = driver.find_element(By.ID, "app-bidlayer-bidsection-input")




while True:
    bid_value = bid_amt + 0.01
    if bid_amt < max_bid and time_left == "1s":
        bid_box.send_keys(bid_value)
        bid_box.send_keys(Keys.RETURN)
        break
    elif bid_amt >= max_bid:
        print("The item has exceeded your maximum price.")
        break
    else:
        continue