# Пульт охраны банка

Сайт с информацией, кто находится в хранилище. 
## Установка 

### Установка python
   
#### Для Linux 
```
sudo apt-get install python3
```
#### Для Mac OC
```
brew install python3
```
## Репозиторий
Клонируйте репозиторий в удобную папку

## Окружение

### Библиотеки

В терминале перейдите в папку с репозиторием.

Установите библиотеки с помощью команды.
```python 
pip3 install -r requirements.txt
```

### Настройки базы данных
#### Обязательные
```python
echo DB_HOST = HOST > .env
echo DB_PORT = PORT >> .env
echo DB_NAME = NAME >> .env
echo DB_USER = USER >> .env
echo DB_PASSWORD = PASSWORD >> .env
```
#### Необязательные
```python
echo DEBUG = (default=False) >> .env
echo ALLOWED_HOSTS = (default='127.0.0.1') >> .env
```

## Запуск 

Для запуска выполните команду в терминале из папки с проектом.
```python
python3 manage.py runserver 0.0.0.0:8000
```
![Результат](https://ltdfoto.ru/images/2023/05/30/django_terminal.png) 

## Результат
Откроется сайт на котором можно посмотреть информацию о посетителях хранилища.
![](https://ltdfoto.ru/images/2023/05/22/site.jpg)