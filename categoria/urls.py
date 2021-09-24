from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.get, name='categoria_list'),
    path('category/<int:id>', views.get, name='categoria_process'),
    path('category/insert/', views.post, name='categoria_insert'),
    path('category/update/<int:id>', views.put, name='categoria_update'),
    path('category/delete/<int:id>', views.delete, name='categoria_delete'),
]