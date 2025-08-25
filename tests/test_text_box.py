from pages.text_box import TextBox
from pages.elements_page import ElementsPage
from pages.form_page import FormPage


def test_check_footer(browser):
    form_page = TextBox(browser)
    form_page.visit()

    def test_login_form(browser):
        text_box = TextBox(browser)

        text_box.visit()
        assert not form_page.modal_dialog.exist()
        text_box.full_name.send_keys('fullName')
        text_box.current_address.send_keys('currentAddress')
        text_box.btn_submit.click_force()

        assert text_box.modal_dialog.exist()
        text_box.btn_close_modal.click_force()


        login_form = FormPage(browser)
        login_form.visit()
        assert login_form.first_name.get_dom_attribute('placeholder') == 'firstName'
        assert login_form.last_address.get_dom_attribute('placeholder') == 'lastName'
        assert login_form.user_email.get_dom_attribute('pattern') == 'userEmail'
