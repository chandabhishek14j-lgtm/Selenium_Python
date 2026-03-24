#how to hande java pop-ups
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url= "https://rahulshettyacademy.com/AutomationPractice/"
my_name = "Abhishek Chand"
driver.get(url)
driver.maximize_window()
your_name = driver.find_element(By.ID,"name")
your_name.send_keys(my_name)
alert = driver.find_element(By.ID,"alertbtn")
alert.send_keys(Keys.RETURN)
time.sleep(3)
aText = driver.switch_to.alert.text
print(aText)
done = driver.switch_to.alert.accept()
time.sleep(3)