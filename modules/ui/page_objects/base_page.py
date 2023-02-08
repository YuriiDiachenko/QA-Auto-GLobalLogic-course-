from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# створення базового класу, який ініціалізує драйвер для роботи з браузером та закриває браузер
class BasePage:
    # властивості класу. PATH - шлях кореневого каталогу проекту
    # DRIVER_NAME -назва файлу нашого драйвера
    PATH = r"/c:/Users/User/Desktop/курс/Git_repository/QA-Auto-GLobalLogic-course-/"
    DRIVER_NAME = 'chromedriver.exe'
    # конструктор класу
    def __init__(self):
        # ініціалізація драйвера для хрому, щоб можна було з ним працювати
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )
    # метод для закриття браузера
    def close(self):
        self.driver.close()
