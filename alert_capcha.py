"""
Нажимаем на кнопку и принимаем алерт браузера для открытия капчи.
Считываем x, высчитываем по формуле ответ и вписываем его в форму. 
После чего подтверждаем отправку формы путем нажатия на кнопку. 
"""
from selenium import webdriver
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    # ждем загрузки страницы
    time.sleep(1)
	
    x_element = browser.find_element_by_id("input_value").text
    y = str(calc(int(x_element)))
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
	
    button2 = browser.find_element_by_class_name("btn")
    button2.click()
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()