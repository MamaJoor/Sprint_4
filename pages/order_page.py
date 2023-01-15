import allure
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ссылка на главную страницу"')
    def get_main_page_url(self):
        self.driver.get(OrderPageLocators.main_page_url)

    @allure.step('Нажатие на кнопку "Заказать" на главной странице')
    def click_main_order_button(self):
        self.driver.find_elements(*OrderPageLocators.main_order_button).click()

    @allure.step('Нажатие на кнопку "Заказать" в шапке страницы')
    def click_header_order_button(self):
        self.driver.find_elements(*OrderPageLocators.header_order_button)[0].click()

    @allure.step('Заполнение поля "Имя"')
    def set_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.first_name_input).send_keys(first_name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_second_name(self, second_name):
        self.driver.find_element(*OrderPageLocators.second_name_input).send_keys(second_name)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(address)

    @allure.step('Заполнение поля "Станция метро"')
    def set_metro(self, metro):
        self.driver.find_element(*OrderPageLocators.metro_input).send_keys(metro)
        self.driver.find_element(*OrderPageLocators.metro_input).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(*OrderPageLocators.metro_input).send_keys(Keys.ENTER)

    @allure.step('Заполнение поля "Телефон"')
    def set_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.phone_number_input).send_keys(phone_number)

    @allure.step('Нажатие на кнопку "Далее"')
    def click_continue_button(self):
        self.driver.find_element(*OrderPageLocators.continue_button).click()

    @allure.step('Заполнение поля "Когда привезти самокат"')
    def set_order_time(self, order_time):
        self.driver.find_element(*OrderPageLocators.order_time_input).send_keys(order_time)
        self.driver.find_element(*OrderPageLocators.order_time_input).send_keys(Keys.ENTER)

    @allure.step('Заполнение поля "Срок аренды"')
    def set_rental_period(self, days):
        self.driver.find_element(*OrderPageLocators.rental_period_choice).click()
        if days == 1:
            self.driver.find_element(*OrderPageLocators.rental_period_one_day).click()
        elif days == 2:
            self.driver.find_element(*OrderPageLocators.rental_period_two_days).click()
        elif days == 3:
            self.driver.find_element(*OrderPageLocators.rental_period_three_days).click()
        elif days == 4:
            self.driver.find_element(*OrderPageLocators.rental_period_four_days).click()
        elif days == 5:
            self.driver.find_element(*OrderPageLocators.rental_period_five_days).click()
        elif days == 6:
            self.driver.find_element(*OrderPageLocators.rental_period_six_days).click()
        elif days == 7:
            self.driver.find_element(*OrderPageLocators.rental_period_seven_days).click()

    @allure.step('Выбор черного самоката')
    def click_color_black(self):
        self.driver.find_element(*OrderPageLocators.color_black).click()

    @allure.step('Выбор серого самоката')
    def click_color_grey(self):
        self.driver.find_element(*OrderPageLocators.color_grey).click()

    @allure.step('Заполнение поля "Комментарий"')
    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.comment_input).send_keys(comment)

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    @allure.step('Нажатие на кнопку "Да"')
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Получить текст о успешно оформленном заказе')
    def get_text_order_status(self):
        return self.driver.find_element(*OrderPageLocators.success_order).text
