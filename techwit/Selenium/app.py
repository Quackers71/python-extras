# Selenium Tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://ec2-18-130-37-136.eu-west-2.compute.amazonaws.com/")