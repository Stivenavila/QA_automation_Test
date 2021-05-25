from selenium.webdriver.common.by import By

from pageobject.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class login(BasePage):
    URL = 'https://serenity.is/demo/'
    User_name = (By.ID, 'StartSharp_Membership_LoginPanel0_Username')
    Password = (By.ID, 'StartSharp_Membership_LoginPanel0_Password')
    Login_click = (By.ID, 'StartSharp_Membership_LoginPanel0_LoginButton')
    Name = (By.XPATH, '//*[@id="StartSharp_Organization_BusinessUnitDialog7_Name"]')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_user(self, user):
        self.driver.find_element(*self.User_name).send_keys(user)

    def set_pass(self, password):
        self.driver.find_element(*self.Password).send_keys(password)

    def set_login(self):
        self.driver.find_element(*self.Login_click).send_keys(Keys.ENTER)

    def set_name(self, name):
        self.driver.find_element(*self.Name).send_keys(name)

    def get_user(self):
        return self.driver.find_element(*self.User_name).get_attribute("value")

    def get_pass(self):
        return self.driver.find_element(*self.Password).get_attribute("value")

    def get_login(self):
        return self.driver.find_element(*self.Login_click).get_attribute("value")

    def get_name(self):
        return self.driver.find_element(*self.Name).get_attribute("value")


class Business(BasePage):
    URL2 = 'https://serenity.is/demo/Organization/BusinessUnit'
    ORG = (By.XPATH, '/html/body/div[2]/aside[1]/section/div/ul/li[6]/a')
    New_bus = (By.XPATH, '/html/body/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[1]')
    save_bus = (By.XPATH, '/html/body/div[5]/div[2]/div/div[1]/div/div/div/div[1]')

    def open2(self):
        self.driver.get(self.URL2)

    def set_ORG(self):
        self.driver.find_element(*self.ORG).click()

    def set_newbus(self):
        self.driver.find_element(*self.New_bus).click()

    def set_savebus(self):
        self.driver.find_element(*self.save_bus).click()

    def get_newbus(self):
        return self.driver.find_element(*self.New_bus).get_attribute("value")

    def get_ORG(self):
        return self.driver.find_element(*self.ORG).get_attribute("value")

    def get_savebus(self):
        return self.driver.find_element(*self.save_bus).get_attribute("value")


class Meeting(BasePage):
    URL3 = 'https://serenity.is/demo/Meeting/Meeting'
    meeti = (By.XPATH, '/html/body/div[2]/aside[1]/section/div/ul/li[5]/a')
    New_mee = (By.XPATH, '/html/body/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[1]')
    Name_mee = (By.ID, 'StartSharp_Meeting_MeetingDialog14_MeetingName')
    Number_mee = (By.ID, 'StartSharp_Meeting_MeetingDialog14_MeetingNumber')
    save_mee = (By.XPATH, '/html/body/div[2]/div[1]/section/div[2]/div[2]/div[1]/div[1]/div/div/div/div[1]')

    def open3(self):
        self.driver.get(self.URL3)

    def set_mee(self):
        self.driver.find_element(*self.meeti).click()

    def get_mee(self):
        return self.driver.find_element(*self.meeti).get_attribute("value")

    def set_newmee(self):
        self.driver.find_element(*self.New_mee).click()

    def get_newmee(self):
        return self.driver.find_element(*self.New_mee).get_attribute("value")

    def set_name(self, name):
        self.driver.find_element(*self.Name_mee).send_keys(name)

    def get_name(self):
        return self.driver.find_element(*self.Name_mee).get_attribute("value")

    def set_number(self, number):
        self.driver.find_element(*self.Number_mee).send_keys(number)

    def get_number(self):
        return self.driver.find_element(*self.Number_mee).get_attribute("value")

    def set_savemee(self):
        self.driver.find_element(*self.save_mee).click()

    def get_savemee(self):
        return self.driver.find_element(*self.save_mee).get_attribute("value")
