from selenium import webdriver


class Driver():
    def __init__(self):
        self.driver = webdriver.Chrome()

browser = Driver().driver


# 等待某个元素出现
