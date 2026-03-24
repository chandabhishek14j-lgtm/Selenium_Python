from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time
import os

driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)
url = "https://rahulshettyacademy.com/upload-download-test/"
driver.get(url)
driver.implicitly_wait(5)
button = wait.until(EC.presence_of_element_located((By.ID, "downloadButton")))
button.click()
file_path = "C:\\Users\\AVITA\\Downloads\\download.xlsx"
while True:
    if os.path.exists(file_path) and not os.path.exists(file_path + ".crdownload"):
        break
    time.sleep(1)
workbook = openpyxl.load_workbook("C:\\Users\\AVITA\\Downloads\\download.xlsx")
sheet = workbook.active
b2 = sheet['B2'].value
B2 = sheet['B2']
rowB = B2.row
colB = B2.column
print(f"{rowB}:type{type(rowB)} , {colB}")
sheet.cell(row=2,column=2).value = "Mango"
workbook.save(file_path)

#upoading a file DOM needs to have a type = file attribute as...
#...selenium on its own can not interact with window
fileElement = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
"""After this we need to send path of the file in send keys method """
fileElement.send_keys(file_path)
toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".Toastify__toast")))
UpdatedText = toast.text
print("Toast found")
print()
SuccessText = "Updated Excel Data Successfully."
assert SuccessText == UpdatedText

#**********Advance way to access table elements in DOM**********

"""
//div[text()='Apple']/parent::div/parent::div/div[@id='cell-4-undefined']
//tag_name[xpath element]/mention parent_tag/mention parent_tag/tag_name[xpath element column in same row]
"""
fruit_name = "Apple"
price_column = driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")
Price = driver.find_element(By.XPATH, "//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+price_column+"-undefined']").text
print(f"{fruit_name} : {Price}")
