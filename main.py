#! /bin/python3

import initial
import os
from page_locators import *
from testmart_pages import *
from testmart_data import *
import time
import unittest


CWD			= os.getcwd()
PROGRAM_FOLDER		= "test"
WEBDRIVER_FOLDER	= "web_driver"
PROGRAM			= "testmart"
WEBDRIVER		= "operadriver"
PATH_TO_PROGRAM		= os.path.join(CWD, PROGRAM_FOLDER)
PATH_TO_WEB_DRIVER	= os.path.join(CWD, WEBDRIVER_FOLDER, WEBDRIVER)


def setUpModule():
	global DRIVER, PROCESS
	PROCESS = initial.start_program(PATH_TO_PROGRAM, PROGRAM)
	time.sleep(3)
	DRIVER = initial.get_driver(PATH_TO_WEB_DRIVER)
	DRIVER.maximize_window()
	time.sleep(3)

def tearDownModule():
	global DRIER, PROCESS
	DRIVER.quit()
	PROCESS.terminate()
	time.sleep(4)


class ATestRegistrationFormTests(unittest.TestCase):

	def setUp(self):
		self.__form = RegistrationForm(DRIVER, "http://localhost:8080/signup")

	def test1(self):
		self.__form.visit_website()
		send_form(self.__form, NO_USERNAME_REGISTER, LOCATOR_REGISTER_BUTTON)
		assert LOCATOR_ERROR_REGISTRATION in DRIVER.page_source

	def test2(self):
		self.__form.visit_website()
		send_form(self.__form, NO_PASSWORD_REGISTER, LOCATOR_REGISTER_BUTTON)
		assert LOCATOR_ERROR_REGISTRATION in DRIVER.page_source

	def test3(self):
		self.__form.visit_website()
		send_form(self.__form, NO_CONFIRM_REGISTER, LOCATOR_REGISTER_BUTTON)
		assert LOCATOR_ERROR_REGISTRATION in DRIVER.page_source

	def test4(self):
		self.__form.visit_website()
		send_form(self.__form, WRONG_PASSWORD_REGISTER, LOCATOR_REGISTER_BUTTON)
		assert LOCATOR_ERROR_REGISTRATION in DRIVER.page_source

	def test5(self):
		self.__form.visit_website()
		send_form(self.__form, WRONG_CONFIRMATION_REGISTER, LOCATOR_REGISTER_BUTTON)
		assert LOCATOR_ERROR_REGISTRATION in DRIVER.page_source

	def test6(self):
		self.__form.visit_website()
		send_form(self.__form, REGISTRATION_OF_NORMAL_ACCOUNT, LOCATOR_REGISTER_BUTTON)
		assert LOCATOR_ERROR_REGISTRATION not in DRIVER.page_source

	def test7(self):
		self.__form.visit_website()
		send_form(self.__form, REGISTRATION_OF_TEST_ACCOUNT, LOCATOR_REGISTER_BUTTON)
		assert LOCATOR_ERROR_REGISTRATION not in DRIVER.page_source

	def test8(self):
		self.__form.visit_website()
		send_form(self.__form, REREGISTRATION_OF_EXISTING_ACCOUNT, LOCATOR_REGISTER_BUTTON)
		assert LOCATOR_ERROR_REGISTRATION in DRIVER.page_source


class BTestLoginForm(unittest.TestCase):

	def setUp(self):
		self.__form = LoginForm(DRIVER, "http://localhost:8080/login")

	def test1(self):
		self.__form.visit_website()
		send_form(self.__form, NO_SUCH_LOGIN, LOCATOR_LOGIN_BUTTON)
		flag = (LOCATOR_ERROR_LOGIN in DRIVER.page_source)
		if not flag:
			self.__form.click_button(LOCATOR_EXIT_ACCOUNT_BUTTON)
		assert flag

	def test2(self):
		self.__form.visit_website()
		send_form(self.__form, NO_PASSWORD_LOGIN, LOCATOR_LOGIN_BUTTON)
		flag = (LOCATOR_ERROR_LOGIN in DRIVER.page_source)
		if not flag:
			self.__form.click_button(LOCATOR_EXIT_ACCOUNT_BUTTON)
		assert flag

	def test3(self):
		self.__form.visit_website()
		send_form(self.__form, NO_USERNAME_LOGIN, LOCATOR_LOGIN_BUTTON)
		flag = (LOCATOR_ERROR_LOGIN in DRIVER.page_source)
		if not flag:
			self.__form.click_button(LOCATOR_EXIT_ACCOUNT_BUTTON)
		assert flag

	def test4(self):
		self.__form.visit_website()
		send_form(self.__form, {}, LOCATOR_LOGIN_BUTTON)
		flag = (LOCATOR_ERROR_LOGIN in DRIVER.page_source)
		if not flag:
			self.__form.click_button(LOCATOR_EXIT_ACCOUNT_BUTTON)
		assert flag

	def test5(self):
		self.__form.visit_website()
		send_form(self.__form, WRONG_LOGIN, LOCATOR_LOGIN_BUTTON)
		flag = (LOCATOR_ERROR_LOGIN in DRIVER.page_source)
		if not flag:
			self.__form.click_button(LOCATOR_EXIT_ACCOUNT_BUTTON)
		assert flag

	def test6(self):
		self.__form.visit_website()
		send_form(self.__form, RIGHT_LOGIN, LOCATOR_LOGIN_BUTTON)
		flag = (LOCATOR_ERROR_LOGIN not in DRIVER.page_source)
		if flag:
			self.__form.click_button(LOCATOR_EXIT_ACCOUNT_BUTTON)
		assert not flag


class CTestBooks(unittest.TestCase):

	def setUp(self):
		self.__form = BooksPage(DRIVER, "http://localhost:8080/books")

	def test1(self):
		self.__form.visit_website()
		list_of_books = self.__form.find_elements(LOCATOR_BOOK)
		for book_element_index in range(len(list_of_books)):
			print(parse_book(self.__form, book_element_index + 1))


if __name__ == "__main__":

	unittest.main(warnings="ignore")
