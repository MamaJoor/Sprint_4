from selenium.webdriver.common.by import By


class HeaderPageLocators:
    main_page_url = "https://qa-scooter.praktikum-services.ru/"
    order_page_url = "https://qa-scooter.praktikum-services.ru/order"

    yandex_logo = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    scooter_logo = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
