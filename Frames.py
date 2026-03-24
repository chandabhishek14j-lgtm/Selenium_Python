#A frame (or iframe) is basically a webpage inside another webpage.
#browser or driver directly can not access iFrame
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
url = "https://the-internet.herokuapp.com/iframe"
driver.get(url)
driver.switch_to.frame("mce_0_ifr")

text_box = wait.until(EC.visibility_of_element_located((By.ID, "tinymce")))
text_box.send_keys(Keys.CONTROL, "a")
text_box.send_keys(Keys.BACKSPACE)
driver.find_element(By.ID, "tinymce").send_keys("I am Abhishek Chand trying frames")
print(text_box.text)
driver.switch_to.default_content() # this will bring you back to browser form frames
