from selenium import webdriver
from details import usernameE, passwordE, usernameL,passwordL


class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:\Program Files\ProgFiles\chromedriver.exe')

    def edureka(self):
        self.driver.get('https://www.edureka.co/')

        login = self.driver.find_element_by_xpath('/html/body/header/nav/ul/li[4]/span')
        login.click()

        user = self.driver.find_element_by_xpath('//*[@id="si_popup_email"]')
        user.click()
        user.send_keys(usernameE)

        pwd = self.driver.find_element_by_xpath('//*[@id="si_popup_passwd"]')
        pwd.click()
        pwd.send_keys(passwordE)

        btn = self.driver.find_element_by_xpath('//*[@id="new_sign_up_optim"]/div/div/div[2]/div[3]/form/button')
        btn.click()

    def leetcode(self):
        self.driver.get('https://leetcode.com/')

        signIn = self.driver.find_element_by_xpath('//*[@id="landing-page-app"]/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[5]')
        signIn.click()

        user = self.driver.find_element_by_xpath('//*[@id="id_login"]')
        user.click()
        user.send_keys(usernameL)

        pwd = self.driver.find_element_by_xpath('//*[@id="id_password"]')
        pwd.click()
        pwd.send_keys(passwordL)

        btn = self.driver.find_element_by_xpath('//*[@id="signin_btn"]/div')
        btn.click()


bot = Bot()
bot.edureka()
# bot.leetcode()