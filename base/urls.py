from django.urls import URLPattern, path
from .  import views

urlpatterns=[
    path("", views.home, name="home"),
    path("addnft/", views.addNFT, name="addnft"),
    path("delete/<str:pk>/", views.delete, name="delete"),
    path("update/<str:pk>/", views.update, name="update"),
]