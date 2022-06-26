from django.urls import path
from blogger import views
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup", views.register, name = "create_user"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
=======
>>>>>>> refs/remotes/origin/main
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> f6ca7e7598b410628912125949f7b288ba679a80

urlpatterns = [
    path("signup", views.register, name = "create_user"),
    path("profile/<pk>/", views.BloggerProfile.as_view(), name="profile"),
    path('editar/<pk>/', views.BloggerUpdate.as_view(), name = "update_profile"),
<<<<<<< HEAD
<<<<<<< HEAD
]
>>>>>>> refs/remotes/origin/main
=======
]
>>>>>>> refs/remotes/origin/main
=======
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

>>>>>>> f6ca7e7598b410628912125949f7b288ba679a80
