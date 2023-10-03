import time


from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_python.darazSignUp import driver


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("https://https://www.daraz.com.np/#")
        self.driver.get("https://www.daraz.com.np/#")

    def teardown(self):
        self.driver.quit()


class TestSignUpPage(BaseTest):

    def test_signUp(self):
        # signUpLink=self.driver.find_elements(By.XPATH,'//*a[@data-tracking-control-name="guest_homepage-basic_nav-header-signin"]')
        signUpLink = driver.find_element(By.ID, "anonSignup")
        signUpLink.click()
        phnum = driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/form/div/div[1]/div[1]/input")
        phnum.send_keys('9869849306')
        fullName = driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/form/div/div[2]/div[1]/input")
        fullName.send_keys("Anusha K.C.")
        time.sleep(3)