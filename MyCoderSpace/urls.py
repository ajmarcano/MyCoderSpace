from django.urls import path
from MyCoderSpace import views

path("", views.BlogList.as_view(), name = "home")
path("create/", views.BlogCreate.as_view(), name = "create")
path("detail/<pk>/", views.BlogDetail.as_view() name = "detail")
path("update/<pk>/", views.BlogUpdate.as_view() name = "update")
path("delete/<pk>/", views.BlogDelete.as_view() name = "delete")


