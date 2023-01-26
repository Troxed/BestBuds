from django.urls import path
from concentrates import views

app_name = "concentrates"

urlpatterns = [
    path("", views.concentrate_list, name="concentrate_list"),
    path("<int:pk>", views.concentrate_detail, name="concentrate_detail"),
    ]
