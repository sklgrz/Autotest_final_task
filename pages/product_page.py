from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def should_be_in_product_page(self):
		self.add_to_basket()
		#self.solve_quiz_and_get_code()
		self.should_be_product_name_in_basket()
		self.should_be_product_price_in_basket()

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
		"Success message is presented, but should not be"

	def should_dissapear_of_success_message(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
		"Success message is not disappeared, but should be"
		
	def add_to_basket(self):
		basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
		basket.click()

	def should_be_product_name_in_basket(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		basket_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
		assert product_name == basket_name, "Product is not in basket"


	def should_be_product_price_in_basket(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text
		assert product_price == basket_price, "Basket price is not equal to product_price"
