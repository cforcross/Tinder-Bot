from selenium import webdriver
from page.HomePage.home_page import Login
from time import sleep
from base.password import password, email
from selenium.webdriver.chrome.options import Options
import time
import unittest


class TinderBot():
    option = Options()

    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(options=self.option)

    def bot(self):
        self.option.add_argument("--disable-infobars")
        self.option.add_argument("start-maximized")
        self.option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        self.option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        baseUrl = "https://tinder.com/"
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(baseUrl)

        face = Login(self.driver)
        sleep(10)
        face.facebook(email=email, password=password)
        face.choice()


ff = TinderBot()
ff.bot()
