# Django REST API с Celery для загрузки и обработки файлов  

Описание
Этот проект представляет собой RESTful API,
созданный с использованием Django и Django REST Framework (DRF).
Он позволяет пользователям загружать файлы на сервер. После загрузки файла на сервер,
он обрабатывается асинхронно с использованием Celery.  

## Основные возможности
Загрузка файлов: Пользователи могут загружать файлы на сервер через эндпоинт upload/.  

Асинхронная обработка: После загрузки файла он отправляется на асинхронную обработку с использованием Celery.  
Это обеспечивает быстрый отклик API, даже если обработка файла занимает много времени.  
Просмотр всех файлов: Эндпоинт files/ позволяет пользователям просматривать список всех загруженных файлов и их статус обработки.  

## Технические детали
Модель File: Эта модель представляет загруженные файлы и содержит следующие поля:  

file: Для загрузки файла.  
uploaded_at: Дата и время загрузки файла.  
processed: Указывает, был ли файл обработан.  
Docker: Проект развертывается с использованием Docker, что обеспечивает легкость и удобство развертывания в любой среде.  

Обработка различных типов файлов: Система способна обрабатывать различные типы файлов, такие как изображения, текстовые файлы и видео.  

Обработка ошибок: В случае ошибок, система возвращает соответствующие коды статуса и сообщения об ошибках.  

## Как запустить
Убедитесь, что у вас установлен Docker.  
Клонируйте репозиторий и перейдите в директорию проекта.  
Запустите docker-compose up для сборки и запуска контейнеров.  
API теперь доступен по адресу http://127.0.0.1:8000/.  

# Тестирование
Для запуска тестов выполните следующую команду:  

docker-compose exec web python manage.py test filer.tests

### Заключение
Этот проект предоставляет надежное и масштабируемое решение для загрузки и обработки файлов.  
С использованием таких инструментов, как Django, DRF и Celery,  
он обеспечивает высокую производительность и асинхронную обработку, что делает его идеальным для реальных сценариев использования.
