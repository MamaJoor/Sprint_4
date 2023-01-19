import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка заказа через кнопку в шапке сайта с 1ым набором данных')
    def test_first_order_header_button(self, driver):
        order_page = OrderPage(driver)
        order_page.get_main_page_url()
        order_page.click_header_order_button()
        order_page.set_first_name('Артем')
        order_page.set_second_name('Жданов')
        order_page.set_address('Фролова, 15')
        order_page.set_metro('Соколники')
        order_page.set_phone_number('79121234567')
        order_page.click_continue_button()

        order_page.set_order_time('09.11.2022')
        order_page.set_rental_period(1)
        order_page.click_color_black()
        order_page.set_comment('Продам гараж')
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.get_text_order_status().startswith('Заказ оформлен')

    @allure.title('Проверка заказа через кнопку в шапке сайта с 2ым набором данных')
    def test_second_order_header_button(self, driver):
        order_page = OrderPage(driver)
        order_page.get_main_page_url()
        order_page.click_header_order_button()
        order_page.set_first_name('Андрей')
        order_page.set_second_name('Бронников')
        order_page.set_address('Бажова, 7')
        order_page.set_metro('Черкизовская')
        order_page.set_phone_number('79129874563')
        order_page.click_continue_button()

        order_page.set_order_time('09.11.2023')
        order_page.set_rental_period(2)
        order_page.click_color_black()
        order_page.set_comment('Куплю гараж')
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.get_text_order_status().startswith('Заказ оформлен')

    @allure.title('Проверка заказа через кнопку на главной странице с 1ым набором данных')
    def test_first_order_main_button(self, driver):
        order_page = OrderPage(driver)
        order_page.get_main_page_url()
        order_page.click_header_order_button()
        order_page.set_first_name('Ждан')
        order_page.set_second_name('Артемов')
        order_page.set_address('Цвиллинга, 7')
        order_page.set_metro('Лубянка')
        order_page.set_phone_number('777777777777')
        order_page.click_continue_button()

        order_page.set_order_time('13.02.2023')
        order_page.set_rental_period(4)
        order_page.click_color_grey()
        order_page.set_comment('Захватите с собой пиццы')
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.get_text_order_status().startswith('Заказ оформлен')

    @allure.title('Проверка заказа через кнопку на главной странице с 2ым набором данных')
    def test_second_order_main_button(self, driver):
        order_page = OrderPage(driver)
        order_page.get_main_page_url()
        order_page.click_header_order_button()
        order_page.set_first_name('Брон')
        order_page.set_second_name('Андреев')
        order_page.set_address('Ленина, 123')
        order_page.set_metro('Комсомольская')
        order_page.set_phone_number('780005553535')
        order_page.click_continue_button()

        order_page.set_order_time('13.04.2023')
        order_page.set_rental_period(5)
        order_page.click_color_grey()
        order_page.set_comment('Захватите с собой роллы')
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.get_text_order_status().startswith('Заказ оформлен')
