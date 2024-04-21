from model.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('John')
    registration_page.fill_last_name('Doe')
    registration_page.fill_email('mail@gmail.com')
    registration_page.fill_gender('Other')
    registration_page.fill_mobile_number('9981111111')
    registration_page.fill_date_of_birth('1999', 'May', '17')
    registration_page.fill_subjects('Maths')
    registration_page.fill_hobbies('Music')
    registration_page.upload_picture('test.jpg')
    registration_page.fill_current_address('test_address')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Panipat')
    registration_page.submit()

    registration_page.should_registered_user_with(
        'John',
        'Doe',
        'mail@gmail.com',
        'Other',
        '9981111111',
        '17 May,1999',
        'Maths',
        'Music',
        'test.jpg',
        'test_address',
        'Haryana',
        'Panipat'
    )
