from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess

driver = webdriver.Firefox()
driver.get('https://www.irctc.co.in/eticketing/loginHome.jsf')

username = driver.find_element_by_name('j_username')
password = driver.find_element_by_name('j_password')
img = driver.find_element_by_name('j_captcha')

username.send_keys('enter_your_username') #replace with your userid
password.send_keys('enter_your_password') #replace with your password

driver.save_screenshot('screenshot.png')
subprocess.call("path_to_bs.sh_file", shell=True) #replace with the path to bs.sh file 
fh = open("tmp.txt", "r")
img.send_keys(fh.readline())
