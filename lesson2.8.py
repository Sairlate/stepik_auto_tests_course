from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("Smolensk@gmail.com")
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")
    path = os.getcwd() + '/' + file.name
    file = browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()