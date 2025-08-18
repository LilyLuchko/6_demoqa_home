from selenium.webdriver.common.by import By
import time
class BasePage:
    def __init__(self,driver,base_url,text_footer,text_center):
        self.driver = driver
        self.base_url = base_url
        self.text_footer = text_footer
        self.text_center = text_center

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR,locator)

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False
    def equal_text_footer(self):
        if self.get_url() == self.text_footer:
            return True
        return False

    def equal_text_center(self):
        if self.get_url() == self.text_center:
            return True
        return False