"""
Нужно заполнить так называемую капчу.
Считываем значение x, высчитываем по формуле calc(x) и вписываем в поле результат.  
Так как нажатие кнопки перекрывает футер, необходимо проскроллить страницу вниз.
Проставляем чекбокс "I'm the robot" и меняем выбор радиобаттона на "Robots rule".
После чего подтвержить отправку формы путем нажатия на кнопку. 
"""

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = str(calc(x))
    
    button = browser.find_element_by_tag_name("button")
    
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    
    option = browser.find_element_by_css_selector("[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option)
    option.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
