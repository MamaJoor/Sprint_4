import allure
from locators.header_page_locators import HeaderPageLocators


class HeaderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ссылка на главную страницу"')
    def get_main_page_url(self):
        self.driver.get(HeaderPageLocators.main_page_url)

    @allure.step('Ссылка на страницу заказа"')
    def get_order_page_url(self):
        self.driver.get(HeaderPageLocators.order_page_url)

    @allure.step('Нажатие на логотип Яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*HeaderPageLocators.yandex_logo).click()

    @allure.step('Нажатие на логотип Самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*HeaderPageLocators.scooter_logo).click()
