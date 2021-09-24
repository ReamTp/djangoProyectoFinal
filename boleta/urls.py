from django.urls import path
from . import views

urlpatterns = [
    path('ticket/', views.get, name='boleta_list'),
    path('ticket/<int:id>', views.get, name='boleta_process'),
    path('ticket/insert/', views.post, name='boleta_insert'),
    path('ticket/update/<int:id>', views.put, name='boleta_update'),
    path('ticket/delete/<int:id>', views.delete, name='boleta_delete'),
]