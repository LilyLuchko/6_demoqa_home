from selenium import webdriver
from selenium.webdriver.common.by import By


def test_icon_exist():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    icon = driver.find_element(By.CSS_SELECTOR,'head > link:nth-child(6)')

    if icon is None:
             print('Иконка не найдена')
    else:
             print('Иконка найдена')

def test_name_exist():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    name = driver.find_element(By.CSS_SELECTOR, '#user-name')

    if name is None:
            print('Имя не найдено')
    else:
            print('Имя найдено')

def test_password_exist():
        driver = webdriver.Chrome()
        driver.get('https://www.saucedemo.com/')

        password = driver.find_element(By.CSS_SELECTOR, '#password')

        if password is None:
            print('Пароль не найден')
        else:
            print('Пароль найден')
