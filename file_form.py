"""
Заполняем текстовую форму и загружаем текстовый файл в форму загрузки файлов.
После чего подтверждаем отправку формы путем нажатия на кнопку. 
"""
from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Smolensk@h.h.ru")
	
	# получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()