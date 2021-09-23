from django.urls import path
from . import views

urlpatterns = [
    path("ciudad/", views.get, name="ciudad_list"),
    path("ciudad/<int:id>",views.get, name="ciudad_uno"),
    path("ciudad/insert/",views.post, name="ciudad_insert"),
    path("ciudad/update/<int:id>", views.put, name="ciudad_update"),
    path("ciudad/activarEstado/<int:id>", views.acEstado, name="ciudad_acEstado"),
    path("ciudad/desactivarEstado/<int:id>", views.desEstado, name="ciudad_desEstado"),
]