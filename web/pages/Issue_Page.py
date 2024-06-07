import time

from web.pages.Base_page import BasePage

class IssuePage(BasePage):

    def add_issue_module(self):
        #进入issue位置
        self.click_element('xpath','//*[@id="已钉选"]/ul/li[1]/a/div[3]/text()')
        time.sleep(1)
        #点击新建议题
        self.click_element('type','//*[@id="content-body"]/div[3]/div/div/section/div[2]/div/a/span')
        #进入新建议题界面
        self.input_data('id','issue_title','the_issue_title')
        self.click_element('xpath','//*[@id="new_issue"]/div[6]/div[1]/div[1]/div/a')
        self.click_element('xpath','//*[@id="new_issue"]/div[7]/button/span')

    def search_issue(self):
        #进入issue位置
        self.click_element('xpath','//*[@id="计划"]/ul/li[1]/a/div[3]/text()')
        #开始查找
        self.input_data('xpath','//*[@id="content-body"]/div[3]/div/div[2]/div[1]/div[2]/div/div/div','the_issue_title')
        time.sleep(1)

    def close_issue(self):
        #进入项目下的issue
        self.find_element('type', '//*[@id="已钉选"]/ul/li[1]/a/div[3]/text()')
        #进入要关闭的issue界面
        self.click_element('xpath','//*[@id="issuable_324"]/div[1]/div[1]/a')
        self.click_element('xpath','//*[@id="dropdown-toggle-btn-42"]/svg')
        self.click_element('xpath','//*[@id="disclosure-43"]/li[3]/button/span')
        #返回列表查看issue
        self.click_element('xpath','//*[@id="disclosure-43"]/li[3]/button/span')

        time.sleep(1)