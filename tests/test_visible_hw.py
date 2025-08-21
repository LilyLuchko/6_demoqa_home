import time
from pages.elements_page import ElementsPage
from pages.accordion import Accordion


def test_visible_according(browser):
    according_page = Accordion(browser)

    according_page.visit()
    assert according_page.visible()

def test_section_heading_click(browser):
    section_heading = Accordion(browser)
    section_heading.visit()
    section_heading.click()
    time.sleep(2)

def test_not_visible_according(browser):
    according_page = Accordion(browser)
    according_page.visit()
    assert not according_page.visible()

def test_visible_accordion_default(browser):
    section_2_content = Accordion(browser)

    section_2_content.visit()
    assert section_2_content.visible()
    assert section_2_content.visible()

    section_2_content_2 = Accordion(browser)

    section_2_content_2.visit()
    assert section_2_content_2.visible()
    assert section_2_content_2.visible()

    section_3_content = Accordion(browser)

    section_3_content.visit()
    assert section_3_content.visible()
    assert section_3_content.visible()
