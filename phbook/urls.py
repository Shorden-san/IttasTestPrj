from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', views.home_page.as_view(), name='home'),
    path('add/', views.AddPhoneView.as_view(), name='add'),
    path('delete/<int:pk>', views.DeletePhoneView.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdatePhoneView.as_view(), name='update')
]