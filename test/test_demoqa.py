import time

from selene import browser, be, have, command
import os


def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element('.text-center').should(have.text('Practice Form'))

    browser.element('#firstName').should(be.blank).set_value('John')
    browser.element('#lastName').should(be.blank).set_value('Doe')
    browser.element('#userEmail').should(be.blank).set_value('test@gmail.com')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').set_value('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="3"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1999"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--010').click()
    browser.element('#subjectsInput').set_value('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test.jpg'))
    browser.element('#currentAddress').set_value('test_address')
    browser.element('#react-select-3-input').set_value('Haryana').press_enter()
    browser.element('#react-select-4-input').set_value('Panipat').press_enter()
    browser.element('#submit').perform(command.js.scroll_into_view).click()
    # browser.element('#submit').click()

    browser.element('.modal-title.h4').should(have.text('Thanks for submitting the form'))
    browser.element('table>tbody>tr:nth-child(1)>td:nth-child(2)').should(have.text('John Doe'))
    browser.element('table>tbody>tr:nth-child(2)>td:nth-child(2)').should(have.text('test@gmail.com'))
    browser.element('table>tbody>tr:nth-child(3)>td:nth-child(2)').should(have.text('Other'))
    browser.element('table>tbody>tr:nth-child(4)>td:nth-child(2)').should(have.text('1234567890'))
    browser.element('table>tbody>tr:nth-child(5)>td:nth-child(2)').should(have.text('10 April,1999'))
    browser.element('table>tbody>tr:nth-child(6)>td:nth-child(2)').should(have.text('Maths'))
    browser.element('table>tbody>tr:nth-child(7)>td:nth-child(2)').should(have.text('Music'))
    browser.element('table>tbody>tr:nth-child(8)>td:nth-child(2)').should(have.text('test.jpg'))
    browser.element('table>tbody>tr:nth-child(9)>td:nth-child(2)').should(have.text('test_address'))
    browser.element('table>tbody>tr:nth-child(10)>td:nth-child(2)').should(have.text('Haryana Panipat'))

