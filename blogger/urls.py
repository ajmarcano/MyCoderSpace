from django.urls import path
from blogger import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup", views.register, name = "create_user"),
    path("profile/<pk>/", views.BloggerProfile.as_view(), name="profile"),
    path('editar/<pk>/', views.BloggerUpdate.as_view(), name = "update_profile"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

