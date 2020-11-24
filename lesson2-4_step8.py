"""
Следим за изменением стоимости дома, как только стоимость дома равна 100$ нажимаем на кнопку.
Появляется стол для заполнения капчи.
Считываем x, высчитываем по формуле ответ и вписываем его в форму. 
После чего подтверждаем отправку формы путем нажатия на кнопку. 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    button = browser.find_element_by_id("book")
    button.click()
    
    x_element = browser.find_element_by_id("input_value").text
    y = str(calc(int(x_element)))
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()