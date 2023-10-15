from selenium import webdriver
from threading import Thread
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


UNAME = input('Enter Username: ')
PSW = input('Enter Password: ')
ActiveThreads = []


def snipe_a_bid(uname, psw):
    url = input("Enter url: ")
    maximum_bid = float(input("Max bid is: "))
    timetobid = input("At how many seconds left do you want to place the bid\n(must be single digit): ")


    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(url)


    def sign_in():
        driver.implicitly_wait(10)
        #login link
        driver.find_element(By.XPATH, r'//*[text()="Sign In"]').click()
        #username
        driver.find_element(By.ID, "username").send_keys(UNAME)
        #password
        driver.find_element(By.ID, "password").send_keys(PSW + Keys.ENTER)
        driver.implicitly_wait(10)
        #submit
    sign_in()


    input("\n\nPRESS ENTER TO CONFIRM YOUR SNIPE ON THIS ITEM AND RETURN TO HOME SCREEN\n\n")
    Thread(target=main, args=(UNAME,PSW)).start()

    while True:
        time_left = driver.find_element(By.XPATH, "//span[@class='detail__time awe-rt-Extended']").text
        if 'Days' in time_left:    
            time_left = time_left.replace('Days ', '')
        else:
            time_left = time_left.replace('Day ', '')

        current_bid = driver.find_element(By.XPATH, "//span[@class='Bidding_Listing_MinPrice awe-rt-MinimumBid']").text
        current_bid = float(current_bid[1:])

        if maximum_bid >= current_bid and time_left[:9] == "0 00:00:0" and int(time_left[9:]) <= int(timetobid):
            # Bid Entry
            driver.find_element(By.ID, "BidAmount").send_keys(str(maximum_bid))
            #Submit button
            driver.find_element(By.ID, "SubmitBid").click()
            #Confirm button
            driver.implicitly_wait(60)
            driver.find_element(By.ID, "modalSubmitButton").click()
            print("\n\nSNIPE SUCCESFUL. BID PLACED\n\n")
            time.sleep(10)
            break
        elif maximum_bid < current_bid:
            print(f"\n\nBID ON THE URL: {url} EXCEEDED YOUR MAXIMUM BID. EXITING NOW.\n\n")
            driver.close()
        else:
            driver.refresh()
            continue




def homescreen():
    print("""
      /$$$$$$                     /$$    /$$                          /$$$$$$          /$$                           
    /$$__  $$                   | $$   |__/                         /$$__  $$        |__/                           
    | $$  \ $$/$$   /$$ /$$$$$$$/$$$$$$  /$$ /$$$$$$ /$$$$$$$       | $$  \__//$$$$$$$ /$$ /$$$$$$  /$$$$$$  /$$$$$$ 
    | $$$$$$$| $$  | $$/$$_____|_  $$_/ | $$/$$__  $| $$__  $$      |  $$$$$$| $$__  $| $$/$$__  $$/$$__  $$/$$__  $$
    | $$__  $| $$  | $| $$       | $$   | $| $$  \ $| $$  \ $$       \____  $| $$  \ $| $| $$  \ $| $$$$$$$| $$  \__/
    | $$  | $| $$  | $| $$       | $$ /$| $| $$  | $| $$  | $$       /$$  \ $| $$  | $| $| $$  | $| $$_____| $$      
    | $$  | $|  $$$$$$|  $$$$$$$ |  $$$$| $|  $$$$$$| $$  | $$      |  $$$$$$| $$  | $| $| $$$$$$$|  $$$$$$| $$      
    |__/  |__/\______/ \_______/  \___/ |__/\______/|__/  |__/       \______/|__/  |__|__| $$____/ \_______|__/      
                                                                                        | $$                        
                                                                                        | $$                        
                                                                                        |__/           """)
    newthread = input("\n\nWould you like to snipe a new auction? [y/n]: ")
    return newthread



def main(uname, psw):
    newthread = homescreen()
    
    if newthread == 'y':
        t = Thread(target=snipe_a_bid, args=(UNAME, PSW))
        t.start()
        t.join()
    elif newthread == 'n':
        input("\n\nIf you have no more active auctions, feel free to close the program.\nIf you do have open auctions, keep this window open and feel free to wait in the homescreen.\nIf you want to snipe another auction or wait in the homescreen.")  



main(UNAME, PSW)
q = input("\n\n|- Press 'x' to quit -|(kill all active bids)\n\
|- Press 's' to add new snipe -| (or wait for active snipe): ")
if q == 's':
    main(UNAME, PSW)
else:
    quit()