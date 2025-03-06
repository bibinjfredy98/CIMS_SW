#GTRE_PROJECT/urls.py


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GTRE_APPLICATION.urls')),
]
