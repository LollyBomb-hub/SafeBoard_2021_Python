#! /bin/python3


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

	def __init__(self, driver, page_url: str) -> None:

		self.__driver = driver
		self.__URL = page_url
		return None

	def find_element(self, locator, timeout=5):
		return WebDriverWait(self.__driver, timeout).until(
						EC.presence_of_element_located(locator),
						message=f"Couldn\'t find element by locator: {locator}"
					)

	def find_elements(self, locator, timeout=5):
		return WebDriverWait(self.__driver, timeout).until(
						EC.presence_of_all_elements_located(locator),
						message=f"Couldn\'t find elements by locator: {locator}"
					)

	def click_button(self, locator, timeout=5):
		return self.find_element(locator, timeout).click()

	def set_text(self, locator, text: str, timeout=5):
		element = self.find_element(locator, timeout)
		element.click()
		return element.send_keys(text)

	def visit_website(self):
		return self.__driver.get(self.__URL)

	def visit(self, page_url):
		return self.__driver.get(page_url)


