import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
 Отправьте полученное число в качестве ответа на это задание.
'''

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Вход в форму и переключение на следующую вкладку
    button1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button1.click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)


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
    if browser.switch_to.alert:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)

    # закрываем браузер после всех манипуляций
    browser.quit()
