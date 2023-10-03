import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.daraz.com.np/#")

signUpLink = driver.find_element(By.ID, "anonSignup")
signUpLink.click()
phnum = driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/form/div/div[1]/div[1]/input")
# phnum = driver.find_element(By.XPATH, "//div[@data-spm-anchor-id='a2o42.login_signup.0.i2.71936af7IHEQEe']//input[type='text']")
phnum.send_keys('9869849306')
fullName = driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/form/div/div[2]/div[1]/input")
fullName.send_keys("Anusha K.C.")
# Vcode = driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[1]/div[2]/div[1]/input")
# Vcode.send_keys('o')
time.sleep(3)



