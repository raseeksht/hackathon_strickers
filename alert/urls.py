from django.urls import path
from . import views

urlpatterns = [
	path('',views.login,name="loginPage"),
	path('services/',views.services,name="servicePage"),
	path('home/',views.home,name="homePage"),
	path('report/',views.report,name="reportPage"),
	path('checktoken/',views.checkToken,name="chtokenpage"),
	path('signup/',views.signup,name="signuppage"),
	path('register/',views.register,name="registerpage"),
]