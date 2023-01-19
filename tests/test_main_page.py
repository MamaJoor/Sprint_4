import allure

from pages.main_page import MainPage



class TestMainPage:
    @allure.title('Проверка ответа на первый вопрос')
    def test_first_question(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page_url()
        main_page.click_cookie_button()
        main_page.scroll_to_questions()
        main_page.click_first_question()
        assert main_page.get_text_first_answer() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка ответа на второй вопрос')
    def test_second_question(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page_url()
        main_page.click_cookie_button()
        main_page.scroll_to_questions()
        main_page.click_second_question()
        assert main_page.get_text_second_answer() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка ответа на третий вопрос')
    def test_third_question(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page_url()
        main_page.click_cookie_button()
        main_page.scroll_to_questions()
        main_page.click_third_question()
        assert main_page.get_text_third_answer() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка ответа на четвертый вопрос')
    def test_fourth_question(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page_url()
        main_page.click_cookie_button()
        main_page.scroll_to_questions()
        main_page.click_fourth_question()
        assert main_page.get_text_fourth_answer() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка ответа на пятый вопрос')
    def test_fifth_question(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page_url()
        main_page.click_cookie_button()
        main_page.scroll_to_questions()
        main_page.click_fifth_question()
        assert main_page.get_text_fifth_answer() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка ответа на шестой вопрос')
    def test_sixth_question(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page_url()
        main_page.click_cookie_button()
        main_page.scroll_to_questions()
        main_page.click_sixth_question()
        assert main_page.get_text_sixth_answer() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка ответа на седьмой вопрос')
    def test_seventh_question(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page_url()
        main_page.click_cookie_button()
        main_page.scroll_to_questions()
        main_page.click_seventh_question()
        assert main_page.get_text_seventh_answer() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка ответа на восьмой вопрос')
    def test_eighth_question(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page_url()
        main_page.click_cookie_button()
        main_page.scroll_to_questions()
        main_page.click_eighth_question()
        assert main_page.get_text_eighth_answer() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'