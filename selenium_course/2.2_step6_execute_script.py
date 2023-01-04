import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
'''
Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером.
'''

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Обработка формулы
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    # Код собирающий переменные
    input1 = browser.find_element(By.ID, 'answer')
    input2 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    input3 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    button = browser.find_element(By.CSS_SELECTOR, "button")

    #Скролинг для скрытия футера


    # Отправляем заполненную форму
    input1.send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input2.click()

    input3.click()
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
