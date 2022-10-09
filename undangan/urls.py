from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('theme2.urls')),
    path('theme2',include('yayarani.urls')),
    path('garcon',include('garcon.urls')),
]
