from django.urls import path
from . import views

urlpatterns = [
	path('',views.login,name="loginPage"),
	path('services/',views.services,name="servicePage"),
	path('home/',views.home,name="homePage"),
]