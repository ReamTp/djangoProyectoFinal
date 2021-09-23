from django.urls import path
from . import views

urlpatterns = [
    path("usuario/", views.get, name="usuario_list"),
    path("usuario/<int:id>",views.get, name="usuario_uno"),
    path("usuario/insert/",views.post, name="usuario_insert"),
    path("usuario/update/<int:id>", views.put, name="usuario_update"),
    path("usuario/activarEstado/<int:id>", views.acEstado, name="usuario_acEstado"),
    path("usuario/desactivarEstado/<int:id>", views.desEstado, name="usuario_desEstado"),
]