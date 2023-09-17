from django.urls import path
from . import views

urlpatterns = [
	path('login/',views.login,name="loginPage"),
	path('',views.index,name="indexPage"),
	path('services/',views.services,name="servicePage"),
	path('home/',views.home,name="homePage"),
	path('report/',views.report,name="reportPage"),
	path('checktoken/',views.checkToken,name="chtokenpage"),
	path('signup/',views.signup,name="signuppage"),
	path('register/',views.register,name="registerpage"),
	path('pendingcases/',views.pendingcase,name="pendingcasepage"),
	path('fetchpendingcase/',views.pendingcase,name="pendingcasepage"),
]