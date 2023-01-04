from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
Это задание с так называемым пир-ревью: правильность вашего решения будут проверять другие учащиеся. Также и вам предстоит проверить чужой код. Ознакомившись с разными способами решения одной и той же задачи, вы сможете лучше понять изучаемую тему.

У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на сайте. Однако разработчики решили немного поменять верстку страницы, чтобы она выглядела более современной. Обновленная страница доступна по другой ссылке. К сожалению, в процессе изменений они случайно внесли баг в форму регистрации.

Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли обнаружить баг, который создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. Пугаться не стоит, здесь ошибка в приложении которое вы тестируете, а не в вашем тесте. 

Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный баг. В этом случае попробуйте поменять селекторы, сделав их уникальными. После изменения убедитесь, что ваш тест исправно проходит в старой версии страницы.

Чтобы получить максимальное количество баллов, прежде чем отправлять решение на рецензию, самостоятельно убедитесь в том что: 

Тест успешно проходит на странице http://suninjuly.github.io/registration1.html﻿

Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html

Используемые селекторы должны быть уникальны

Будьте внимательны, ведь на рецензирование работу можно отправить только один раз! 

Прикрепите файл с тестом к этому заданию, а затем отправьте его на рецензирование. Убедитесь что расширение файла .py а не .txt, иначе велика вероятность, что ваше решение не запустится у других. Убедитесь, что в вашем коде не указаны пути до хромдрайвера, иначе ваш код не запустится у других студентов. Если вы используете Firefox или что-то, что мы не проходили в курсе, добавьте комментарии о том, как запустить такой код. Помните, что ваш код будут проверять, в том числе, новички.

Не забудьте посмотреть и отрецензировать работы других учащихся, только после этого вы получите баллы за данное задание. 

Кстати! Не удаляйте код после прохождения задания, он нам пригодится в будущих модулях. 
'''

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1, value2, value3 = '.first[placeholder*="name"]', '.second[placeholder*="name"]', '.third[placeholder*="email"]'

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, value3)
    input3.send_keys("noname@name.ru")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()