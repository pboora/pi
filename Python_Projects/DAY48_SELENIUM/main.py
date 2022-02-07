# #### Seleinum web driver Web Scraping#####
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("/Users/bakul/Desktop/xcode/appbrewery/aatmja/pi/Python_Projects/DAY48_SELENIUM/chromedriver/chromedriver")
driver = webdriver.Chrome(service=serv)

driver.get("https://www.amazon.co.uk/Samsung-Galaxy-Mobile-Phone-Smartphone/dp/B08FT71HH5/ref=sr_1_1?keywords=samsung%2Bs20&qid=1638851050&sr=8-1")
price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print("Check", price.tag_name)
print(price.get_attribute('innerHTML'))