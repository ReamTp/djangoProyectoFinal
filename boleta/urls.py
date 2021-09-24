from django.urls import path
from . import views

urlpatterns = [
    path('', views.get, name='boleta_list'),
    path('<int:id>/', views.get, name='boleta_process'),
    path('insert/', views.post, name='boleta_insert'),
    path('update/<int:id>', views.put, name='boleta_update'),
    path('delete/<int:id>', views.delete, name='boleta_delete'),
]