from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getIndexPage, name = 'indexPage'),
    path('<page>', views.getPage, name = 'statisticPage')
]