from web.pages.Main_page import loginPage
from web.pages.Project_page import *
from web.pages.Issue_Page import *
from web.pages.Search_page import *
import pytest
import time
class TestAll(BasePage):
    #该方法在全部测试中只调用一次,即只登录一次
    #@classmethod
    def setup_class(cls):
        cls.login_page = loginPage()
        cls.login_page.open_login_page()
        cls.login_page.login_module()

    """def test_001_login(self):
        login_page = loginPage()
        login_page.open_login_page()
        login_page.login_module()"""

    def test_002_add_project(self):

        self.add_page = AddProjectPage()
        self.add_page.add_project_module()

    def test_003_add_issue(self):

        self.add_issue = IssuePage()
        self.add_issue.add_issue_module()


    def test_004_search_issue_success(self):
        self.search_issue_success = IssuePage()
        self.search_issue_success.search_issue()
        self.new_ele = self.find_element('xpath','//ul[@class="content-list issuable-list issues-list"]//li//a[@data-testid="issuable-title-link"]')
        if self.new_ele != None:
            assert f"该issue存在"
        else:
            assert f"该issue不存在"

    def test_005_close_issue(self):
        self.close_issue = IssuePage()
        self.close_issue.close_issue()
        self.new_ele = self.find_element('xpath','//*[@id="content-body"]/div[3]/div/section/div[2]/div/a')
        assert self.new_ele != None


