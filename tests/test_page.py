import pytest
from time import sleep
from selenium import webdriver

from pageobject.Conten_page import login
from pageobject.Conten_page import Business
from pageobject.Conten_page import Meeting


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="Drive/chromedriver.exe")
    yield driver
    sleep(1)
    driver.quit()


def test_file_login(browser):
    Login_page = login(browser)
    Login_page.open()
    Login_page.set_user('admin')
    Login_page.set_pass('serenity')
    Login_page.set_login()
    sleep(3)
    Business_page = Business(browser)
    Business_page.set_ORG()
    Business_page.open2()
    Business_page.set_newbus()
    sleep(10)
    Login_page.set_name('Test')
    Business_page.set_savebus()
    sleep(2)
    Meeting_page = Meeting(browser)
    Meeting_page.set_mee()
    Meeting_page.open3()
    Meeting_page.set_newmee()
    Meeting_page.set_name('test')
    Meeting_page.set_number('541651')
    Meeting_page.set_savemee()
