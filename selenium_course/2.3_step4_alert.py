import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
 вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
'''

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Вход в форму
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    # Обработка формулы
    x_elem = browser.find_element(By.ID, "input_value")
    x = calc(x_elem.text)

    # Код собирающий переменные
    input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")

    # Отправляем заполненную форму
    input1.send_keys(x)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
