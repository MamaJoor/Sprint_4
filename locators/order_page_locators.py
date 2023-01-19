from selenium.webdriver.common.by import By


class OrderPageLocators:
    main_page_url = "https://qa-scooter.praktikum-services.ru/"

    header_order_button = [By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"]
    main_order_button = [By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']/button[text() = 'Заказать']"]
    first_name_input = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    second_name_input = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    address_input = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    metro_input = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    metro_row = [By.CLASS_NAME, "select-search__row"]
    phone_number_input = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    continue_button = [By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')]"]
    order_time_input = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    rental_period_choice = [By.XPATH, ".//div[text() = '* Срок аренды']"]
    rental_period_one_day = [By.XPATH, ".//div[text() = 'сутки']"]
    rental_period_two_days = [By.XPATH, ".//div[text() = 'двое суток']"]
    rental_period_three_days = [By.XPATH, ".//div[text() = 'трое суток']"]
    rental_period_four_days = [By.XPATH, ".//div[text() = 'четверо суток']"]
    rental_period_five_days = [By.XPATH, ".//div[text() = 'пятеро суток']"]
    rental_period_six_days = [By.XPATH, ".//div[text() = 'шестеро суток']"]
    rental_period_seven_days = [By.XPATH, ".//div[text() = 'семеро суток']"]
    color_black = [By.ID, "black"]
    color_grey = [By.ID, "grey"]
    comment_input = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"]
    order_button = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Заказать']"]
    yes_button = [By.XPATH, ".//button[text() = 'Да']"]
    success_order = [By.XPATH, ".//div[text() = 'Заказ оформлен']"]
    view_status_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[2]/button']