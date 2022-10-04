from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def should_be_basket_page(self):
		self.should_be_empty_basket()
		self.should_be_row_with_the_text_about_the_basket_is_empty()

	def should_be_empty_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), \
		"Basket is not empty, but should be"

	def should_be_row_with_the_text_about_the_basket_is_empty(self):
		assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_ROW), \
		"Row with the text about the basket is empty wasn't appeared, but should be"
