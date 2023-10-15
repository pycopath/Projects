import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = input("Paste the url to the item: ")
maximum_bid = float(input("max bid is: "))
user = input("Enter username: ")
psw = input("Enter password: ")
# 
#
#CHANGE STRING VARIABLE FOR HIGHER PRICED ITEMS
#CHANGE STRING VARIABLE FOR HIGHER PRICED ITEMS
#CHANGE STRING VARIABLE FOR HIGHER PRICED ITEMS
#
#
#

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(url)


# log into my account
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


tag = driver.find_element(By.CLASS_NAME, "x-additional-info__textual-display",)
tag = tag.text
tag = str(tag)
string = tag[:0] + tag[10:]
string = string[:5] #CHANGE VARIABLE FOR HIGHER PRICED ITEMS


#Create a function that finds the current price
current_price = float(string)
        #do other things to notify(email?)

run = True

outbidded1 = driver.find_element(By.ID, "vi-statusmessage-panel-content")
outbidded2 = str(outbidded1.text)[:18]
while run==True:
    bidTooHigh = False
    driver.refresh()
# Check if the current price is under the maximum price
# and if I've been outbidded
    if current_price < maximum_bid and outbidded2 == "You've been outbid":
        bid_box = driver.find_element(By.ID, "MaxBidId")
        bid_value = current_price + 0.01
        bid_box.send_keys(bid_value)
        bid_button = driver.find_element(By.ID, "bidBtn_btn")
        bid_button.click()
        driver.implicitly_wait(10)
        confirm_bid = driver.find_element(By.ID, "confirm_button")
        confirm_bid.click()
        time.sleep(1)
        close = driver.find_element(By.CLASS_NAME, "vilens-modal-close")
        close.click()
    while outbidded2 == "You're the high bi":
        print("You hold the highest bid.")
        driver.implicitly_wait(10)
        driver.refresh()
        
    if outbidded2 == "":
        print("YOU HAVE NOT BIDDED YET")
        break
    else:
        print('Bid has exceeded maximum profitable price.')
        bidTooHigh = True
    if bidTooHigh == True:
        print("closed tab and ended program")
        break
    else:
        time.sleep(5)
        continue
