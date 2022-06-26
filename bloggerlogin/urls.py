from django.urls import path
from bloggerlogin import views

urlpatterns = [

    path("login/", views.BlogLogin.as_view(), name = "login"),
    path("logout", views.BlogLogout.as_view(), name='logout'),

]