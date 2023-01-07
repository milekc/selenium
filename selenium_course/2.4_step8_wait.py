import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

'''
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
'''

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
#button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #Ожидание цены 100 и нажатие кнопки
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    print(price)
    button = browser.find_element(By.ID, "book")
    button.click()

    # скролл до формулы
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # обработка формулы и заполнение полей
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(calc(x))
    button1 = browser.find_element(By.ID, "solve")
    button1.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # if browser.switch_to.alert:
    #     alert = browser.switch_to.alert
    #     alert_text = alert.text
    #     print(alert_text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)

    # закрываем браузер после всех манипуляций
    browser.quit()
