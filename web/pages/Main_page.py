import time
import pytest
from web.pages.Base_page import BasePage


class loginPage(BasePage):
    def __init__(self):
        self.url = 'https://contest.gitlab.ceba.ceshiren.com/users/sign_in'

    def open_login_page(self):
        self.open(self.url)
        time.sleep(2)


    def login_module(self):
        self.input_data("id","user_login",'384451819@qq.com')
        self.input_data('id','user_password','Hogwarts2024')
        self.click_element('xpath','/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/form/button')
        time.sleep(2)
