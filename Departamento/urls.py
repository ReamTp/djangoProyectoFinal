from django.urls import path
from . import views

urlpatterns = [
    path("departamento/", views.get, name="departamento_list"),
    path("departamento/<int:id>",views.get, name="departamento_uno"),
    path("departamento/insert/",views.post, name="departamento_insert"),
    path("departamento/update/<int:id>", views.put, name="departamento_update"),
    path("departamento/activarEstado/<int:id>", views.acEstado, name="departamento_acEstado"),
    path("departamento/desactivarEstado/<int:id>", views.desEstado, name="departamento_desEstado"),
]