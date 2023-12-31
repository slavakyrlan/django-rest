"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from film.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FilmAPIList.as_view()), #FilmAPIView post #api/filmlist/
    path('api/filmlist/<int:pk>/', FilmAPIUpdate.as_view()), #PUT http://127.0.0.1:8000/api/filmlist/25/
    path('api/filmdetail/<int:pk>/', FilmAPIDetailView.as_view()), # get http://127.0.0.1:8000/api/filmdetail/1/
    # http://127.0.0.1:8000/api/filmdetail/60/ delete
]

# http://127.0.0.1:8000/api/filmlist/ - post