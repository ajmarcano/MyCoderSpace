from django.urls import path
from blogger import views

urlpatterns = [
    path("crear/", views.SignUpView.as_view(), name = "create_user"),
    path("profile/<pk>/", views.BloggerProfile.as_view(), name="profile"),
    path('editar/<pk>/', views.BloggerUpdate.as_view(), name = "update_profile"),
]