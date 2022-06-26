from django.urls import path
from MyCoderSpace import views

urlpatterns = [
    path("pages", views.BlogList.as_view(), name = "home"),
    path("create/", views.BlogCreate.as_view(), name = "create"),
    path("pages/<pk>/", views.BlogDetail.as_view(), name = "detail"),
    path("update/<pk>/", views.BlogUpdate.as_view(), name = "update"),
    path("delete/<pk>/", views.BlogDelete.as_view(), name = "delete"),
    path('About/', views.About, name="about"),
    path('', views.Home, name="principal"),
]

