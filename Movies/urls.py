from django.urls import path, include
from django.contrib import admin
from films.views import Create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('films.urls')),
    path('create/', Create),
]
