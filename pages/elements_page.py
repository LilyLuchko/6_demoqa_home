from pages.base_page import BasePage
class ElementsPage(BasePage):
    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver,self.base_url)
        self.text_footer = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
        self.text_center = 'Please select an item from left to start practice.'