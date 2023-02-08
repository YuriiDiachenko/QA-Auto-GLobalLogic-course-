from modules.ui.page_objects.sign_in_page import SignInPage # імпорт класу, який відпрвідає за функціонування входу в систему
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():

    #створення об'єкту сторінки з імпортованого класу
    sign_in_page = SignInPage()

    #виклик методу відкриття сайту
    sign_in_page.go_to()

    #виклик методу введеня логіна та паролю, та натискання кнопки"увійти"
    sign_in_page.try_login('page_object@gmail.com', 'wrong password')

    #перевірка співпадання назви заголовка сторінки з очікуваним результатом
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    #виклик методу закриття браузера
    sign_in_page.close()
