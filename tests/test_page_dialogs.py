from pages.modal_dialogs import ModalDialogs
from pages.elements_page import ElementsPage


def test_modal_elements(browser):
    modal_elements = ModalDialogs(browser)
    modal_elements.visit()

    assert modal_elements.btn_sub_menu.check_count_elements(count = 5)


def test_navigation_modal(browser):
    modal_navigation = ModalDialogs(browser)
    modal_navigation.visit()
    modal_navigation.refresh()
    modal_navigation.icon.click()
    browser.back()
    browser.set_window_size(900,400)
    browser.forward()
    assert modal_navigation.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000,1000)


















