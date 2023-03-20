from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home_page.as_view(), name='home'),
    path('accounts/', include("accounts.urls"), name='account'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('add/', views.AddPhoneView.as_view(), name='add'),
    path('delete/<int:pk>', views.DeletePhoneView.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdatePhoneView.as_view(), name='update')
]