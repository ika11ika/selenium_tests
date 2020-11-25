"""
Считываем два числа,высчитываем их сумму.   
В выпадающем списке выбираем элемент со значем посчитанной суммы. 
Подтверждаем отправку формы путем нажатия на кнопку. 
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
 
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = int(browser.find_element_by_id("num1").text)
    x2_element = int(browser.find_element_by_id("num2").text)
    x = str(x_element + x2_element)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x) # ищем элемент с текстом "Python"
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()