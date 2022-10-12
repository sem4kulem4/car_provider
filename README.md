# Управление заказами автомобилей

Django-приложение, которое решает задачу по управлению заказами на автомобили поставщика.

### Клонирование репозитория
```
git clone git@github.com:sem4kulem4/car_provider.git
```
### Запуск и установка контейнера

```
cd infra/
sudo docker-compose up -d --build
sudo docker-compose exec web python manage.py makemigrations 
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py collectstatic --no-input
```
Если нужна админка, то создать пользователя в терминале
```
sudo docker-compose exec web python manage.py createsuperuser
```
Отключение контейнеров/отключение контейнеров с очисткой томов
```
sudo docker-compose down
sudo docker-compose down -v
```

### Документация
```
http://127.0.0.1/redoc/
```

### GitHub
```
https://github.com/sem4kulem4
```
