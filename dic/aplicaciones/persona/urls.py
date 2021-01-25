from django.contrib import admin
from django.urls import path
from django.views.generic.base import View

from . import views

urlpatterns = [
    path('lempleado/', views.listAllEmpleados.as_view()),
    #shortname es un parametro que se le pasa a la vista en el metodo get_queryset
    path('empbyarea/<shortname>/', views.listByArea.as_view()),
    path('emp_clave/', views.ListEmpleadoByKword.as_view()),
    path('habilemp/', views.ListHabilidadesEmpleado.as_view()),
]
