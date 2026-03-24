from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
url = "https://rahulshettyacademy.com/loginpagePractise/"
driver.get(url)
driver.maximize_window()

userName = ""
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
openWindows = driver.window_handles
driver.switch_to.window(openWindows[1])
bodyText = driver.find_element(By.XPATH, "//p[@class='im-para red']").text

words = bodyText.split()
print(words)
userName = words[4]
print(userName)
driver.close()
driver.switch_to.window(openWindows[0])

driver.find_element(By.ID, "username").send_keys(userName)
driver.find_element(By.ID, "password").send_keys(12345678)
check = driver.find_element(By.XPATH, "(//label[@class='customradio'])[2]")
check.click()
okayButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-success")))
okayButton.click()
wait.until(EC.invisibility_of_element((By.CSS_SELECTOR,".modal-content")))
checkBox = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
checkBox.click()
print(checkBox.is_selected())
driver.find_element(By.ID, "signInBtn").click()

try:
    alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
    print("Error message:", alert.text)
except TimeoutException:
    print("No error alert found")
    print("Maybe login succeeded")
    print("Current URL:", driver.current_url)

