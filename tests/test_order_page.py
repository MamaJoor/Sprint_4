import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка заказа через кнопку в шапке сайта')
    def test_first_order(self, driver):
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

    @allure.title('Проверка заказа через кнопку на главной странице')
    def test_second_order(self, driver):
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
