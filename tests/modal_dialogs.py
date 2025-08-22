from pages.base_page import BasePage
from components.components import WebElement
# import time
class ModalDialogs(BasePage):
    def __init__(self,driver): #,text_footer,text_center
        self.driver = driver
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btn_sub_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')  # здесь указываю локатор из лекции,
        self.icon = WebElement(driver, 'header > a > img')
        # так как у меня сейчас не доступен demoqa.com, не могу посмотреть правильный локатор
