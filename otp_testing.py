from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import send_it
#from selenium.webdriver.chrome.options import Options
import os

#from pyvirtualdisplay import Display
from selenium.webdriver import Firefox






def send_desired_email(otp_recieved,emailed):
	#chrome_options = Options()
	#chrome_options.add_argument("--headless")
	#chrome_options.add_argument('--headless')
	#chrome_options.add_argument("--window-size=1920x1080")
	#chrome_options.add_argument("--disable-extensions")
	#display = Display(visible=0, size=(800, 600))
	#display.start()
	#chrome_driver = os.getcwd() +"\\geckodriver.exe"
	#browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=chrome_driver)    #remove from line 14 to 16 to unhide     browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)


	browser=webdriver.Chrome('C:\\Users\\aayush\\Desktop\\MAJOR_PROJECT1\\chromedriver.exe')
	try:
		browser.get("https://mail.yahoo.com/")
#sign_in = browser.find_element_by_('Sign input')                        
#sign_in.click()  														# go to sign in page 
#time.sleep(2) 
		sign=browser.find_element_by_link_text('Sign in')
		sign.click()
		time.sleep(2)                                        
		company_email=browser.find_element_by_id("login-username")
		company_email.send_keys('fetch_show@yahoo.com')                                 # enter email id   
		time.sleep(2)
		browser.find_element_by_id("login-signin").submit()

#browser.get("https://accounts.google.com/signin/v2/sl/pwd?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward")
		time.sleep(2)                                                     #helps the browser to load and wait for new page to open and adapt to the new page opened
		password_official=browser.find_element_by_id("login-passwd")                                           

		password_official.send_keys("Hora_Hora")                     # enter password    
		password_official.send_keys(Keys.ENTER)
#time.sleep(2)
#next_button=browser.find_element_by_xpath('''//*[@id="login-signin"]''')
#next_button.click()              
		time.sleep(10)                                                
		new_message=browser.find_element_by_link_text("Compose")  
		new_message.click()
		time.sleep(10)
		username=browser.find_element_by_id("message-to-field")                      #the user we want to send otp
		username.send_keys(emailed)
		message=browser.find_element_by_xpath('''//*[@id="mail-app-component"]/div/div/div[1]/div[3]/div/div/input[@data-test-id="compose-subject"]''')        #message to be sent , ie , OTP
		message.send_keys('YOUR VERIFICATION CODE!!')
		message1=browser.find_element_by_xpath('''//*[@id="editor-container"]/div[@data-test-id="rte"]''')        #message to be sent , ie , OTP
		message1.send_keys('YOUR VERIFICATION CODE IS '+str(otp_recieved ))


		browser.find_element_by_xpath('''//*[@id="mail-app-component"]/div/div/div[2]/div[2]/div/button[@data-test-id="compose-send-button"]''').click()

		browser.close()
		#display.stop()

	except Exception:



		browser.close()
		#display.stop()
		send_it.sending_mail(otp_recieved,emailed)
		
