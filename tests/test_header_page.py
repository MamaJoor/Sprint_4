import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.header_page import HeaderPage


class TestHeaderPage:
    @allure.title('Проверка нажатия на логотип яндекса')
    def test_click_yandex_logo(self, driver):
        header_page = HeaderPage(driver)
        header_page.get_main_page_url()
        header_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 3).until(EC.url_to_be('https://dzen.ru/?yredirect=true'))
        assert driver.current_url == "https://dzen.ru/?yredirect=true"

    @allure.title('Проверка нажатия на логотип самоката')
    def test_click_scooter_logo(self, driver):
        header_page = HeaderPage(driver)
        header_page.get_order_page_url()
        header_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
