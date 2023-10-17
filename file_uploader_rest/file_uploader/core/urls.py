from django.contrib import admin
from django.urls import path
from filer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_file, name='Загрузить файл в базу'),
    path('files/', views.list_files, name='Получить все объекты из базы'),
]
