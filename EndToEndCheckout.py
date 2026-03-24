from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
import openpyxl
import os
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
driver.maximize_window()

#using partial characters in CSS or XPATH to obtain element
"""
xpath: //a[contains(@href,'shop')] | //tag_name[contains(@attribute_name, 'attribute_value')]
css  : a[href*='shop'] | tag_name[attribute_name*='attribute_value']
"""
shop_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='shop']")))
shop_button.click()
shop_url = driver.current_url
assert "shop" in shop_url

visible_items = driver.find_elements(By.XPATH, "//app-card/div[@class='card h-100']")
for item in visible_items:
    title = driver.find_element(By.XPATH, ".//h4[@class='card-title']/a").text
    if title != "Blackberry":
        print("Not Blackberry!! Pass")
    else:
        add_button = driver.find_element(By.XPATH, ".//button[@class='btn btn-info']")
        add_button.click()

checkout = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav-link.btn.btn-primary")))
checkout.click()

final_checkout = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-success")))
final_checkout.click()

location = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".validate")))
location.send_keys("India")
suggestion = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='India']")))
dynamicText = driver.find_element(By.XPATH, "//a[text()='India']").get_attribute("textContent")
try:
    assert dynamicText == "India"
    print("Success")
except AssertionError:
    print("Test Fail")
suggestion.click()

purchase = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
purchase.click()

try:
    alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
    print("Success message:", alert.text)
except TimeoutException:
    print("No error alert found")
    print("Purchase not Done")
    

