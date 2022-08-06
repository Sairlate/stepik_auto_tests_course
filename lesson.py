from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]').send_keys("Ivan")
    time.sleep(1)
    input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]').send_keys("Petrov")
    time.sleep(1)
    input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]').send_keys("Smolensk@gmail.com")
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")


    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()