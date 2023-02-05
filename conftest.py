import pytest # імпорт модуля pytest
from modules.api.clients.github import GitHub # імпорт класу GitHub з файлу github.py



class User:  # ініціалізація класа

    def __init__ (self): # конструктор класа
        self.name = None # поле класа, зі значенням за замовченням 
        self.second_name = None # поле класа, зі значенням за замовченням 

    def create(self): # метод об'єкта, який створює новий екземпляр (об'єкт) класа
        self.name = 'Yurii' # параметр об'єкта з визначенним значенням
        self.second_name = 'Diachenko' # параметр об'єкта з визначенним значенням

    def remove(self): # метод об'єкта, який міняє значення полів об'єкта на пусті значення
        self.name = ''
        self.second_name = ''


@pytest.fixture # декоратор фікстури
def user(): # опис фікстури
    user = User() # створення об'єкта класа
    user.create() # виклик методу об'єкта

    yield user #  виконання тесту, в якому була викликана ця фікстура

    user.remove() # виклик методу об'єкта

@pytest.fixture # декоратор фікстури
def github_api(): # ініціалізація та подальший опис фікстури
    api = GitHub() # виклик класу GitHub, який ми в 2 рядку імпортували
    yield api # виконання тесту, в якому була викликана ця фікстура
