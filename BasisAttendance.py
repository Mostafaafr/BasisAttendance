# A program to automate my attendance since I'm always forgetting
from selenium import webdriver
import time, datetime, pyautogui, sys

driver = webdriver.Chrome(r'chromedriver.exe')

def openUrl(url):
    driver.get(url)
    driver.fullscreen_window()


def login():
    f = open("loginCredentials.txt", "r")
    username = driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div/div[1]/div/input')
    username.send_keys(f.readline())

    password = driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div/div[2]/div/input')
    password.send_keys(f.readline())

    loginButton = driver.find_element_by_xpath('//*[@id="root"]/div/div/form/div/button')
    loginButton.click()

    time.sleep(2) #required to allow schedule screen to load


def openSchedule():
    schedule = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/a[2]')
    schedule.click()


def chooseDay():
    monday = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/a[1]')
    tuesday = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/a[2]')
    wednesday = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/a[3]')
    thursday = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/a[4]')
    friday = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[1]/a[5]')

    dow = datetime.datetime.today().weekday() #gets the current day as an integer
    if dow == 0:
        monday.click()
    elif dow == 1:
        tuesday.click()
    elif dow == 2:
        wednesday.click()
    elif dow == 3:
        thursday.click()
    elif dow == 4:
        friday.click()

    time.sleep(1)


def checkAttendance():
    x = 2930 #the x and y coordinates of the first join button
    y = 575
    rgb = (34, 186, 70) #the color of the join button

    while True:
        if pyautogui.pixelMatchesColor(x, y, rgb):  #the join buttons move depending on various factors, so we simply check every 10 pixels for the color of the join button and click it
            pyautogui.click(x, y)
            driver.quit()
            sys.exit() #the program exits once attendance is checked
        
        if y == 865:
            pyautogui.click(x,y)
            pyautogui.scroll(-200)
        y = y + 10



if __name__=="__main__":
    openUrl("https://spork.school")
    login()
    openSchedule()
    chooseDay()
    checkAttendance()
