from django.urls import path
from . import views

urlpatterns = [
    path('', views.garcon, name="garcon"),
    path('index', views.index, name="index"),
    path('features-type', views.featuresType, name="features-type"),
    path('pageapp-userlist', views.pageappUserList, name="pageapp-userlist"),
]
