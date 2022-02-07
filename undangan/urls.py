from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('yayarani.urls')),
    path('theme2',include('theme2.urls')),
]
