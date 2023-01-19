from selenium.webdriver.common.by import By


class MainPageLocators:
    main_page_url = "https://qa-scooter.praktikum-services.ru/"
    yandex_page_url = "https://dzen.ru/?yredirect=true"

    cookie_button = [By.ID, "rcc-confirm-button"]
    accordion = [By.CLASS_NAME, 'Home_FAQ__3uVm4']
    first_question = [By.ID, "accordion__heading-0"]
    second_question = [By.ID, "accordion__heading-1"]
    third_question = [By.ID, "accordion__heading-2"]
    fourth_question = [By.ID, "accordion__heading-3"]
    fifth_question = [By.ID, "accordion__heading-4"]
    sixth_question = [By.ID, "accordion__heading-5"]
    seventh_question = [By.ID, "accordion__heading-6"]
    eighth_question = [By.ID, "accordion__heading-7"]
    first_answer = [By.ID, "accordion__panel-0"]
    second_answer = [By.ID, "accordion__panel-1"]
    third_answer = [By.ID, "accordion__panel-2"]
    fourth_answer = [By.ID, "accordion__panel-3"]
    fifth_answer = [By.ID, "accordion__panel-4"]
    sixth_answer = [By.ID, "accordion__panel-5"]
    seventh_answer = [By.ID, "accordion__panel-6"]
    eighth_answer = [By.ID, "accordion__panel-7"]
