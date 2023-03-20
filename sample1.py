from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
#from selenium.webdriver.common.by import By ChromeDriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(options=Options())
driver.get("https://www.google.com")

#driver2 = webdriver.Firefox(options=Options())
#driver2 = webdriver.Firefox()
#driver2.get("https://dev.to")
#driver2.find_element_by_id("nav-search").send_keys("Selenium")

search_field = driver.find_element(By.TAG_NAME, "input")
search_field.send_keys("selenium")
search_field.send_keys(Keys.ENTER)

driver.close()
#driver2.close()
