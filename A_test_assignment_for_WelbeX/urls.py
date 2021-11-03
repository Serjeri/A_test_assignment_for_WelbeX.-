from django.conf.urls import url
from django.urls import path
from . import views
from django_filters.views import FilterView

urlpatterns = [
    path('', views.index),
    path('httpResponse/', views.httpResponse),
]