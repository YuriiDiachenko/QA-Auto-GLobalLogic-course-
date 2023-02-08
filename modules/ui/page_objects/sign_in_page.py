from modules.ui.page_objects.base_page import BasePage # імпорт створення базової сторінки
from selenium.webdriver.common.by import By # імпорт модуля для пошуку елементів за певними атрибутами

#створення класу, який відповідає за перевірку функціоналу входу в систему
class SignInPage(BasePage):
    URL = 'https://github.com/login'

    # цей клас наслідує клас BasePage, який ми імпортували
    def __init__(self):
        super().__init__()

    #метод об'єкту, який переходить на певний сайт
    def go_to(self):
        self.driver.get(SignInPage.URL)

    # метод об'єкту, який виконує пошук та заповнення полів "логін" "пароль",
    # та після цього натискає кнопку "увійти"
    def try_login(self, username, password):
        #пошук поля "логін" на сторінці
        login_elem = self.driver.find_element(By.ID, "login_field")
        # ввід в поле "логін" аргумента метода 'username'
        login_elem.send_keys(username)
        # пошук поля "пароль" на сторінці
        pass_elem = self.driver.find_element(By.ID, 'password')
        # ввід в поле "пароль" аргумента метода 'password'
        pass_elem.send_keys(password)
        # пошук поляк "увійти" на сторінці
        btn_elem = self.driver.find_element(By.NAME, 'commit')
        # натискання кнопки "увійти"
        btn_elem.click()

    # метод об'єкта, який порівнює заголовок сторінки сайта з аргументом методу
    def check_title(self, expected_title):
        return self.driver.title == expected_title
