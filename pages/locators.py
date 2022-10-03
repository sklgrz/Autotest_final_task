from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
	BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
	BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner strong')
	BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
	PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
	PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
