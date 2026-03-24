from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://rahulshettyacademy.com/client"
driver.get(url)

driver.find_element(By.CSS_SELECTOR,".login-wrapper-footer-text").send_keys(Keys.RETURN)
print(driver.current_url)
if "register" in driver.current_url:
    driver.find_element(By.ID, "firtname").send_keys("Abhishek")
    driver.find_element(By.ID, "lastName").send_keys("Abhishek")
    driver.find_element(By.ID, "userEmail").send_keys("Abhishek")
    driver.find_element(By.ID, "userMobile").send_keys("Abhishek")
    dropdown = Select(driver.find_element(By.CSS_SELECTOR,".custom-select ng-valid ng-touched ng-dirty"))
    dropdown.select_by_visible_text("Engineer")
    driver.find_element(By.XPATH, "//input[@value='Male']").click()
    driver.find_element(By.ID, "userPassword").send_keys("Alpha@1234")
    driver.find_element(By.ID, "confirmPassword").send_keys("Alpha@1234")
    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    driver.find_element(By.XPATH, "//input[@value='Register']").click()

driver.quit()