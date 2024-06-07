from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from web.drivers.driver import browser
from selenium.webdriver.common.by import By


class BasePage():
    #打开指定url的网页
    def open(self,url):
        browser.get(url)

    #定位元素
    def find_element(self,type,value):
        if type == 'id':
            el = browser.find_element(By.ID,value)
        elif type == 'name':
            el = browser.find_element(By.NAME,value)
        elif type == 'class':
            el = browser.find_element(By.CLASS_NAME, value)
        elif type == 'link':
            el = browser.find_element(By.LINK_TEXT,value)
        elif type == 'plink':
            el = browser.find_element(By.PARTIAL_LINK_TEXT,value)
        elif type == 'css':
            el = browser.find_element(By.CSS_SELECTOR,value)
        elif type == 'xpath':
            el = browser.find_element(By.XPATH,value)
        else:
            print('输入的定位方式有误')
        return el

    #点击目标元素
    def click_element(self,type,value):
        self.find_element(type,value).click()

    #向目标元素输入文本
    def input_data(self,type,value,text):
        self.find_element(type,value).send_keys(text)

    #鼠标移动到目标元素上悬停
    def move_mouse_to_element(self,type,value):
        ActionChains(browser).move_to_element(self.find_element(type,value)).pause(2).perform()

    #选择下拉菜单
    def select_value(self,type,value,text):
        Select(self.find_element(type,value)).select_by_visible_text(text)

    #切换框架
    def switch_to_frame(self,id_name_or_element):
        browser.switch_to.frame(id_name_or_element)

    #切换窗口
    def switch_to_window(self,title):
        handles = browser.window_handles
        for handle in handles:
            browser.switch_to.window(handle)
            if browser.title == title:
                break

    #删除全部cookie
    def del_cookie(self):
        browser.delete_all_cookies()