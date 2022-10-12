# Управление заказами автомобилей

Django-приложение, которое решает задачу по управлению заказами на автомобили поставщика.


### Запуск и установка контейнера

```
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py makemigrations 
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py collectstatic --no-input
```
Если нужна админка, то создать пользователя в терминале
```
sudo docker-compose exec web python manage.py createsuperuser
```

### Документация
```
http://127.0.0.1/redoc/
```

### GitHub
```
https://github.com/sem4kulem4
```
