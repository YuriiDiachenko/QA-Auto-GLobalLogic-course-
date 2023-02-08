import pytest

from selenium import webdriver # модуль для комунікації з драйвером браузера
from selenium.webdriver.common.by import By # модуль для пошуку елементів за певними атрибутами
from selenium.webdriver.chrome.service import Service # модуль для керування браузером ХРОМ!!


@pytest.mark.ui
def test_check_incorrect_username():
    #створення об'єкту для керування браузером ХРОМ за допомогою selenium
    driver = webdriver.Chrome(
        service=Service(r'/c:/Users/User/Desktop/курс/Git_repository/QA-Auto-GLobalLogic-course-/' + 'chromedriver.exe')
    )
    #метод get - відкриває сторінку в браузері (якщо браузер закритий - то його буде відкрито)
    driver.get('https://github.com/login')
    #метод find_element - шукає елемент (по його унікальних параметрах) на сторінці
    login_elem = driver.find_element(By.ID, 'login_field')
    #метод send.keys - передає дані в певний елемент
    login_elem.send_keys('ergerg@gmail.com')
    #метод find_element - шукає елемент (по його унікальних параметрах) на сторінці
    pass_elem = driver.find_element(By.ID, 'password')
    #метод send.keys - передає дані в певний елемент
    pass_elem.send_keys('wrong password')
    #метод find_element - шукає елемент (по його унікальних параметрах) на сторінці
    btn_elem = driver.find_element(By.NAME, 'commit')
    #метод click - імітує "натискання" лівої кнопки миші
    btn_elem.click()
    #метод title - по
    assert driver.title == 'Sign in to GitHub · GitHub'
    #метод clodse - закриває браузер
    driver.close()
