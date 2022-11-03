from . import views
from django.urls import path
urlpatterns =[
    path("", views.index, name='home'),
    path("investment", views.investment, name='investment'),
    path("about", views.about, name='about'),
    path("deposite", views.deposite, name='deposite'),
    path("profile", views.profile, name='profile'),
    path("withdraw", views.withdraw, name='withdraw'),
    path("login_register", views.login_register, name='login_register'),
    path('register/', views.registerpage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('machine/<str:pk>/', views.machine, name="machine"),
    path('process/', views.updateItem, name="process,"),

]