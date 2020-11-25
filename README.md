# selenium_tests
Тесты для веб-страниц проекта https://github.com/SunInJuly/SunInJuly.github.io        
Для запуска тестов потребуется установленная версия Python (не менее 3.7.3) и Selenium (3.14.0)

```
# Модуль Selenium для Python можно установить следующей командой:
pip install selenium==3.14.0
```

Скачивание драйвера. Так как тесты настроены под Сhromedriver, потребуется его скачать.   
Скачать можно [здесь](https://sites.google.com/a/chromium.org/chromedriver/downloads)   
Для Windows достаточно просто поместить скачанный exe в папку с файлом python.exe.   
Команды для Linux можно найти по [ссылке](https://stepik.org/lesson/25969/step/9)

Каждый файл запускается отдельно, тестируются разные веб-страницы, частично имеющие общий функционал.    
Логика тестов для каждого из файлов.    

alert_capcha.py    
Нажимаем на кнопку и принимаем алерт браузера для открытия капчи. Считываем x, высчитываем по формуле ответ и вписываем его в форму. После чего подтверждаем отправку формы путем нажатия на кнопку.    

capcha.py   
Заполняем капчу. Считываем значение x, высчитываем по формуле calc(x) и вписываем в поле результат. Необходимо поставить чекбокс "I'm the robot" и поменять выбор радиобаттона на "Robots rule". После чего подтвержить отправку формы путем нажатия на кнопку.    

capcha_image_attr.py   
Заполняем капчу.Считываем значение x, заложенное в атрибуты картинки, высчитываем по формуле calc(x) и вписываем в поле результат. Необходимо поставить чекбокс "I'm the robot", поменять выбор радиобаттона на "Robots rule" и подтвердить отправку формы путем нажатия на кнопку.    

check_reg_form.py   
Тест на заполнения только обязательных полей. Проверяем отправку формы нажатием на кнопку.   

file_form.py   
Заполняем текстовую форму и загружаем текстовый файл в форму загрузки файлов. После чего подтверждаем отправку формы путем нажатия на кнопку. Файл file.txt удже добавлен в репозиторий для успешного прохождения данного теста.    
form_find_button.py   
Тест на заполнение формы. Отправку формы производим именно на кнопку Submit. Кнопку Submit находим путем прямой ссылки XPath.   

formx100.py   
Ищем и заполняем все поля для ввода, которые только надем на странице (по умолчанию на странице их 100 штук). Подтверждаем отправку формы нажатием на кнопку.   

implicit_button_capcha.py   
Следим за изменением стоимости дома, как только стоимость дома равна 100$ нажимаем на кнопку. Появляется слот для заполнения капчи. Считываем x, высчитываем по формуле ответ и вписываем его в форму. Подтверждаем отправку формы путем нажатия на кнопку. 

link_form.py   
Нужно найти зашифрованную ссылку и кликнуть по ней. Откроется форма, её необходимо заполнить и отправить. Текст ссылки, которую нужно найти, зашифрован формулой, заложенной в страницу: 
str(math.ceil(math.pow(math.pi, math.e)*10000))   

newtab_capcha.py   
Нажимаем на кнопку и принимаем предложение браузера об открытии новой вкладки. Переходим в открывшуюся вкладку для заполнения капчи. Считываем x, высчитываем по формуле ответ и вписываем его в форму. Подтверждаем отправку формы путем нажатия на кнопку.    

scroll_capcha.py   
Заполняем капчу. Считываем значение x, высчитываем по формуле calc(x) и вписываем в поле результат. Так как нажатие кнопки перекрывает футер, необходимо проскроллить страницу вниз. Проставляем чекбокс "I'm the robot" и меняем выбор радиобаттона на "Robots rule". Подтверждаем отправку формы путем нажатия на кнопку.   

select_sum.py    
Считываем два числа, высчитываем их сумму. В выпадающем списке выбираем элемент со значем посчитанной суммы. Подтверждаем отправку формы путем нажатия на кнопку.    
