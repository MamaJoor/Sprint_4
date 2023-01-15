import allure
from time import sleep
from pages.header_page import HeaderPage


class TestHeaderPage:
    @allure.title('Проверка нажатия на логотип яндекса')
    def test_click_yandex_logo(self, driver):
        header_page = HeaderPage(driver)
        header_page.get_main_page_url()
        header_page.click_yandex_logo()
        sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        assert driver.current_url.__contains__('https://dzen.ru/?')

    @allure.title('Проверка нажатия на логотип самоката')
    def test_click_scooter_logo(self, driver):
        header_page = HeaderPage(driver)
        header_page.get_order_page_url()
        header_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
