"""
Нужно заполнить так называемую капчу х2.
Считываем значение x, заложенное в атрибуты картинки, высчитываем по формуле calc(x) и вписываем в поле результат.  
Необходимо поставить чекбокс "I'm the robot" и поменять выбор радиобаттона на "Robots rule".
После чего подтвержить отправку формы путем нажатия на кнопку. 
"""
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name("img").get_attribute("valuex")
    x = x_element
    y = str(calc(x))
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    option = browser.find_element_by_id("robotCheckbox")
    option.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()