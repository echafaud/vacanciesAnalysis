from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getIndexPage),
    path('<page>', views.getPage)
]