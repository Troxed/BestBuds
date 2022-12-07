from django.urls import path
from strains import views

app_name = "strains"

urlpatterns = [
    path("", views.strain_list, name="strain_list"),
    path("<int:pk>", views.strain_detail, name="strain_detail"),
    path('<int:pk>/delete/', views.strain_delete, name='strain_delete'),
    path('<int:pk>/edit/', views.strain_edit, name='strain_edit'),
    path('add-strain/', views.add_strain, name='add_strain'),
]
