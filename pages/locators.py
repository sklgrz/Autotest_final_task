from selenium.webdriver.common.by import By


class BasePageLocators():
	BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn-default')
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	BASKET_EMPTY_ROW = (By.XPATH, r"//div[@id='content_inner']/p")
	BASKET_FORM = (By.ID, "basket_formset")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL = (By.NAME, 'registration-email')
    REGISTER_PASSWORD_1 = (By.NAME, 'registration-password1')
    REGISTER_PASSWORD_2 = (By.NAME, 'registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')

class ProductPageLocators():
	BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
	BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner strong')
	BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
	PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
	PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
	SUCCESS_MESSAGE = (By.CLASS_NAME, 'fade')
