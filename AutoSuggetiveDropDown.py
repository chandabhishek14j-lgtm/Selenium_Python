from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/dropdownsPractise/"
driver.get(url)
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)

country = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
#this will find multiple elements and select first
count = len(country) # return list of all elements present
print(count)

for item in country:
    cText = item.text
    if cText == "India":
        item.click()
        break
#dynamic text cannot be retrieved with the .text
#if I want to print autosuggestive text to get that text we use getattribute("value")
dynamicText = driver.find_element(By.ID,"autosuggest").get_attribute("value")
print(dynamicText)
try:
    assert dynamicText == "India"
    print("Success")
except AssertionError:
    print("Test Fail")

#dynamic dropdown
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkBox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for item in checkBox:
    if item.get_attribute("value") == "option2":
        item.click()
        try:
            assert item.is_selected()
            print("Success!!!")
        except AssertionError:
            print("Test Fail")
        break
time.sleep(3)

rButton = driver.find_elements(By.CSS_SELECTOR,".radioButton")
rButton[0].click()
try:
    assert rButton[0].is_selected()
    print("!!!Success!!!")
except AssertionError:
    print("Test Fail")