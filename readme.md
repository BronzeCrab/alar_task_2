## Задание

II. Python, асинхронные запросы.

- Есть три удаленных источника данных (в качестве источников для тестового задания то могут быть два статических JSON файла на том же сервере с массивом простых данных - ID и некое текстовое поле, содержащее в теле ID). Пример: 
[ 
{“id”:1,”name”:”Test 1”}, 
{“id”:2,”name”:”Test 2”} 
] 
Источники доступны по HTTP. 
В данных для каждого элемента должен быть ID. 
ID распределены следующим образом: 
- 1-й источник: ID 1-10,31-40; 
- 2-й источник: ID 11-20,41-50; 
- 3-й источник: ID 21-30,51-60; 
- Есть одна общая точка доступа до этих данных (приложение Flask или Django), которая выдаёт коррелированный результат. 
Точка доступна по HTTP. 
- Эта точка должна делать запросы ко всем источникам одновременно (асинхронно) и ждать результата со всех. 
- По получению результата от всех, выдать отсортированный по ID результат (данные со всех источников). 
- Ошибка от любого из источников игнорируется и интерпретируется, как отсутствие данных. Ошибкой также считается таймаут (2 секунды).

## Как запустить:

- pip3 intall -r requirements.txt
- sudo apt-get install rabbitmq-server
- celery -A alar_task_2 worker -l info