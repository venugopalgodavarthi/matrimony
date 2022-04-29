from django.urls import path
from authe import views
app_name='authe'
urlpatterns=[
    path('register/',views.registerview,name="register"),
    path('login/',views.loginview,name="login"),
    path('logout/',views.logoutview,name="logout"),
    path('home/',views.homeview,name="home"),
]