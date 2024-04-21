from model.user import User, user_test
from model.registration_page import RegistrationPage


def test_registration():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.register(user_test)

    registration_page.submit()

    registration_page.should_have_registered(user_test)
