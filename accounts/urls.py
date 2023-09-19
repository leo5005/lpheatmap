from django.urls import path
from accounts import views

urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='account_logout'),
]