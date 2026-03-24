from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).send_keys(Keys.RETURN).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
