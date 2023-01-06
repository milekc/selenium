import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

1) Открыть страницу http://suninjuly.github.io/file_input.html
2) Заполнить текстовые поля: имя, фамилия, email
3) Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4) Нажать кнопку "Submit"

Если все сделано правильно и быстро, вы увидите окно с числом.
Отправьте полученное число в качестве ответа для этого задания.
'''

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код собирающий переменные
    input1 = browser.find_element(By.NAME, 'firstname')
    input2 = browser.find_element(By.NAME, 'lastname')
    input3 = browser.find_element(By.NAME, 'email')
    load_file = browser.find_element(By.NAME, 'file')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    # Обработка файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)

    # Отправляем заполненную форму
    input1.send_keys('Ivan')
    input2.send_keys('Ivanov')
    input3.send_keys('ivanov@ivanov.com')
    load_file.send_keys(file_path)
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
