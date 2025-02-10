import allure
from conftest import *

class TestClass:

    @allure.title("Sign In test")
    @allure.epic("Log in/Log out Tests")
    @allure.feature("Log in")
    def test_sign_in(self, login):
        assert sign_in(login) == "Swag Labs"

    @allure.title("Sign Out test")
    @allure.epic("Log in/Log out Tests")
    @allure.feature("Log out")
    def test_sign_out(self, login):
        assert sign_out(login) == "Swag Labs"
