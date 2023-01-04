import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return int(x) + int(y)


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Обработка формулы
    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text

    # Ваш код, который заполняет обязательные поля
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(calc(x, y)))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
