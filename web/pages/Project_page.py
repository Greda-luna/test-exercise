import time
from web.pages.Base_page import BasePage

class AddProjectPage(BasePage):
    def add_project_module(self):
        #判断是否有已经建好的项目
        self.new_project = self.find_element('css','#content-body > div.page-title-holder.gl-display-flex.gl-align-items-center > div > a.gl-button.btn.btn-md.btn-confirm > span')
        if self.new_project != None:
            self.click_element('xpath','//*[@id="content-body"]/div[2]/div/a[2]/span/text()')
            self.click_element('css', '#content-body > div.project-edit-container > div:nth-child(2) > div.gl-display-flex.gl-flex-direction-column > div:nth-child(2) > div:nth-child(1) > a > div.gl-pl-4 > h3')
            time.sleep(1)

        else:
            # 开始创建空白项目
            self.click_element('xpath', '//*[@id="content-body"]/div[2]/div[2]/div[2]/div[1]/div[1]/a/div[2]/h3')
            time.sleep(1)
        #输入项目名字
        self.input_data('id','project_name','the_need_name')
        time.sleep(1)
        #点击创建按钮
        self.click_element('xpath','//*[@id="new_project"]/button/span')
        time.sleep(1)


