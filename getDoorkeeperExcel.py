from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

display = Display(visible=0, size=(1024, 768))
display.start()

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",0)
fp.set_preference("browser.download.manager.showWhenStarting",True)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=utf-8")

driver = webdriver.Firefox(fp)

driver.get("https://manage.doorkeeper.jp/user/sign_in")
driver.find_element_by_id("user_email").click()
driver.find_element_by_id("user_email").clear()
driver.find_element_by_id("user_email").send_keys("change_mail_address")
driver.find_element_by_id("user_password").click()
driver.find_element_by_id("user_password").clear()
driver.find_element_by_id("user_password").send_keys("change_password")
driver.find_element_by_name("commit").click()
time.sleep(2)
driver.get("change_url")
time.sleep(60)
driver.close()
display.stop()