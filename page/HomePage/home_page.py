from base.web_driver import SeleniumWebDriver
import time


class Login(SeleniumWebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ####           ######
    ###locators#####
    ####            #######

    fbk_login = "/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button/span[2]"
    fbk_email = '//*[@id="email"]'
    fbk_pass = '//*[@id="pass"]'
    fbk_login_button = '//*[@id="u_0_0"]'
    location_pop = '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span'
    notification = '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span'

    like_button = '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button'
    dislike_button = '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button'
    close_pop_up = '//*[@id="modal-manager"]/div/div/div[2]/button[2]'
    found_match = '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a'

    def facebook_pop(self):
        self.elementClick(self.fbk_login, locatorType="xpath")

    def switch_me(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        return base_window

    def re_switch_me(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(base_window)

    def facebook_email(self, email):
        self.sendKeys(email, self.fbk_email, locatorType="xpath")

    def facebook_pass(self, password):
        self.sendKeys(password, self.fbk_pass, locatorType="xpath")

    def facebook_button(self):
        self.elementClick(self.fbk_login_button, locatorType="xpath")

    def click_location_pop(self):
        self.elementClick(self.location_pop, locatorType="xpath")

    def click_notification(self):
        self.elementClick(self.notification, locatorType='xpath')

    ###         ####
    # Choice Methods
    ###         ####

    def like_me(self):
        self.elementClick(self.like_button, locatorType='xpath')

    def dislike_me(self):
        self.elementClick(self.dislike_button, locatorType='xpath')

    def click_close_pop_up(self):
        self.elementClick(self.close_pop_up, locatorType='xpath')

    def click_found_match(self):
        self.elementClick(self.found_match, locatorType='xpath')

    def facebook(self, email, password):
        self.facebook_pop()
        self.switch_me()
        self.facebook_email(email)
        self.facebook_pass(password)
        self.facebook_button()
        self.re_switch_me()
        self.click_location_pop()
        self.click_notification()

    def choice(self):
        time.sleep(10)
        self.like_me()
        # while True:
        #     time.sleep(5)
        #     try:
        #         self.like_me()
        #     except AttributeError:
        #         try:
        #             self.click_close_pop_up()
        #         except AttributeError:
        #             self.click_found_match()
        #
