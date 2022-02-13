from django.urls import path
from . import views

urlpatterns = [
    path('', views.theme2, name="theme2"),
    path('<message>/', views.theme2, name="theme2"),
    path('create2', views.create2, name="create2"),
]
