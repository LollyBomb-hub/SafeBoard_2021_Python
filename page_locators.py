#! /bin/python3


from selenium.webdriver.common.by import By


LOCATOR_NAME			= (By.XPATH, "//*[@id=\"name\"]")
LOCATOR_USERNAME		= (By.XPATH, "//*[@id=\"username\"]")
LOCATOR_PASSWORD		= (By.XPATH, "//*[@id=\"password\"]")
LOCATOR_CONFIRM_PASSWORD	= (By.XPATH, "//*[@id=\"password-confirm\"]")
LOCATOR_REGISTER_BUTTON		= (By.XPATH, "//*[@id=\"app\"]/section/div/div[2]/div/div/div[2]/form/div[5]/div[2]/div/div/button")
LOCATOR_LOGIN_BUTTON		= (By.XPATH, "//*[@id=\"submit\"]")
LOCATOR_EXIT_ACCOUNT_BUTTON	= (By.XPATH, "//*[@id=\"signout\"]")


LOCATOR_BOOK			= (By.CLASS_NAME, "media")
LOCATOR_BOOKNAME		= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/div[1]/div/h2")
LOCATOR_AUTHOR			= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/div[1]/div/p[1]")
LOCATOR_DESCRIPTION		= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/div[1]/div/p[2]")
LOCATOR_ISBN13			= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/figure/p[2]")
LOCATOR_ISBN10			= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/figure/p[3]")
LOCATOR_STARS			= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/div[1]/div/div/div/div[1]/img")
LOCATOR_TEXT_UNDER_STARS	= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/div[1]/div/div/div/div[2]/small")
LOCATOR_PRICE			= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/div[2]/div/div[1]/p[1]/strong")
LOCATOR_OLD_PRICE		= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/div[2]/div/div[1]/p[2]/small/span")
LOCATOR_ADD_TO_CART_BUTTON	= (By.XPATH, f"//*[@id=\"app\"]/section/article[%d]/div[2]/div/div[2]/div/a")


LOCATOR_ERROR_LOGIN		= "Не правильный Username или Password."
LOCATOR_ERROR_REGISTRATION	= "Укажите Username и Password."


