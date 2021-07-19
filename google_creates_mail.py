from selenium import webdriver
from mail_info import info
from Data_File import Data_file
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

info()
my_file = Data_file()
keyboard = Controller()


def keyboard_input(text):
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.2)


def keyboard_down(count):
    for i in range(count):
        keyboard.press("\r")
        keyboard.release("\r")
        time.sleep(2)


browser = webdriver.Chrome('chromedriver.exe')
browser.maximize_window()
browser.get('https://account.mail.ru/signup')

# This inputs First name of the user.

WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="fname"]'))).click()
keyboard_input("Joel")

# This inputs Last name of the user.

WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="lname"]'))).click()
keyboard_input("Wade")

# These inputs user's day, month and year of user.

keyboard_input("\t ")
keyboard_down(1)
keyboard_input("\t ")
keyboard_down(1)
keyboard_input("\t ")
keyboard_down(1)

# This clicks on the "male" box.
Gender = browser.find_element_by_xpath(
    '/html/body/div[1]/div[3]/div[3]/div[2]/div/div/div/form/div[8]/div[2]/div/label[2]/div[1]/div[2]')
Gender.click()

# This choose the first defined Account name.
keyboard_input("\t ")
WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="aaa__input"]'))).click()
keyboard_down(1)

# This inputs the email account password.
WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="password"]'))).click()
keyboard_input("JW123654789!@#")

# This re-enters the created password.
WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="repeatPassword"]'))).click()
keyboard_input("JW123654789!@#")

# This inputs a rеquired and existing mail to specify the creating one.
specify_email = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[2]/div/div/div/form/div[17]/span')
specify_email.click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="extra-email"]'))).click()
keyboard_input("znshan@mail.ru")
