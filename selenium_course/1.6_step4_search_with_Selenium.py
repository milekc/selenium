import time

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium. Если всё сделано правильно, то вы увидите окно с проверочным кодом. Это число вам нужно ввести в качестве ответа в этой задаче.

!Обратите внимание, что время для ввода данных ограничено. Однако благодаря Selenium вы сможете выполнить задачу до того, как время истечёт.

Для решения этой задачи мы подготовили для вас шаблон кода, в который нужно только подставить нужные значения для поиска вместо слов value1, value2 и т.д. Обратите внимание, что значения нужно заключать в кавычки, т.к. они должны передаваться в виде строки.
'''

link = "http://suninjuly.github.io/simple_form_find_task.html"
value1, value2, value3 = "input", "last_name", "city"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
