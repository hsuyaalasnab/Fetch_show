from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


def give_directions(line1,line2,line4):
	try:
		browser = webdriver.Chrome('C:\\Users\\aayush\\Desktop\\MAJOR_PROJECT1\\chromedriver.exe')
		browser.get('https://www.google.com/maps')
		directi=browser.find_element_by_id("searchbox-directions")
		directi.click()
		time.sleep(6)
		location1=browser.find_element_by_xpath('''//*[@id="sb_ifc51"]/input[@class="tactile-searchbox-input"]''')

		location1.send_keys('tri nagar,delhi')


		location1.send_keys(Keys.ENTER)

		location2=browser.find_element_by_xpath('''//*[@id="sb_ifc52"]/input[@placeholder="Choose destination, or click on the map..."]''')
		location2.send_keys(str(line2)+','+str(line4))
		location2.send_keys(Keys.ENTER)
	except Exception:
		pass
