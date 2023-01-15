import allure
from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ссылка на главную страницу"')
    def get_main_page_url(self):
        self.driver.get(MainPageLocators.main_page_url)

    @allure.step('Нажатие на кнопку принять соглашение cookie')
    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.cookie_button).click()

    @allure.step('Пролистать то таблицы с вопросами')
    def scroll_to_questions(self):
        accordion = self.driver.find_element(*MainPageLocators.accordion)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion)

    @allure.step('Нажатие на первый вопрос')
    def click_first_question(self):
        self.driver.find_element(*MainPageLocators.first_question).click()

    @allure.step('Нажатие на второй вопрос')
    def click_second_question(self):
        self.driver.find_element(*MainPageLocators.second_question).click()

    @allure.step('Нажатие на третий вопрос')
    def click_third_question(self):
        self.driver.find_element(*MainPageLocators.third_question).click()

    @allure.step('Нажатие на четвертый вопрос')
    def click_fourth_question(self):
        self.driver.find_element(*MainPageLocators.fourth_question).click()

    @allure.step('Нажатие на пятый вопрос')
    def click_fifth_question(self):
        self.driver.find_element(*MainPageLocators.fifth_question).click()

    @allure.step('Нажатие на шестой вопрос')
    def click_sixth_question(self):
        self.driver.find_element(*MainPageLocators.sixth_question).click()

    @allure.step('Нажатие на седьмой вопрос')
    def click_seventh_question(self):
        self.driver.find_element(*MainPageLocators.seventh_question).click()

    @allure.step('Нажатие на восьмой вопрос')
    def click_eighth_question(self):
        self.driver.find_element(*MainPageLocators.eighth_question).click()

    @allure.step('Получить текст первого ответа')
    def get_text_first_answer(self):
        return self.driver.find_element(*MainPageLocators.first_answer).text

    @allure.step('Получить текст второго ответа')
    def get_text_second_answer(self):
        return self.driver.find_element(*MainPageLocators.second_answer).text

    @allure.step('Получить текст третьего ответа')
    def get_text_third_answer(self):
        return self.driver.find_element(*MainPageLocators.third_answer).text

    @allure.step('Получить текст четвертого ответа')
    def get_text_fourth_answer(self):
        return self.driver.find_element(*MainPageLocators.fourth_answer).text

    @allure.step('Получить текст пятого ответа')
    def get_text_fifth_answer(self):
        return self.driver.find_element(*MainPageLocators.fifth_answer).text

    @allure.step('Получить текст шестого ответа')
    def get_text_sixth_answer(self):
        return self.driver.find_element(*MainPageLocators.sixth_answer).text

    @allure.step('Получить текст седьмого ответа')
    def get_text_seventh_answer(self):
        return self.driver.find_element(*MainPageLocators.seventh_answer).text

    @allure.step('Получить текст восьмого ответа')
    def get_text_eighth_answer(self):
        return self.driver.find_element(*MainPageLocators.eighth_answer).text
