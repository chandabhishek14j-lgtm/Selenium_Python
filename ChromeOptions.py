from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--start-maximized')
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--ignore-certificate-errors')
chromeOptions.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chromeOptions)
