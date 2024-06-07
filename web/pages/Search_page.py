import time

from web.pages.Base_page import BasePage

class SearchPage(BasePage):

    def search_device_module(self):
        print('搜索模块')
        time.sleep(1)

    def del_rule_module(self):
        print('删除业务模块')
        time.sleep(1)