from django.urls import include

from django.contrib import admin
from django.urls import path
from phbook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('phbook.urls'))
]


