from django.views.generic.list import MultipleObjectTemplateResponseMixin
from aplicaciones.departamento.models import Departamento
from django.shortcuts import render

from django.views.generic import (ListView)
#models
from .models import Empleado

# Create your views here.

#listar todos los empleados de la empresa
class listAllEmpleados(ListView):
    """lista todos los empleados"""
    template_name = "persona/list_all.html"
    #haremos una paginación para ver como ser realiza el metodo de paginacion
    paginate_by = 4
    #p_num = self.request.GET.get("kword",'')
    model = Empleado
    
#listar todos los empleados que pertenecen a un area de la empresa
class listByArea(ListView):
    #usamos el queryset envez del modelo para trabajar con varios tablas
    """ queryset = Empleado.objects.filter(
        departamento__shortname = 'otro',
    )
    """
    template_name = "persona/lbyarea.html"
    
    #lo anterior es la peor manera de ralizar un queryset, veamos cual es la MultipleObjectTemplateResponseMixin
    def get_queryset(self):
        #en la variable area recuperamos el parametro shortname qeu le emos enviado en la url
        #con el metodo sefl.kwargs recuperamos todos los parametros qaue vienen de esa url
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__shortname = area #en vez de definir el area de la empresa le pasamos el valor qaue tiene area. lo que recuperamos en la url
        )
        return lista

#listar empelaos por palabra clave
class ListEmpleadoByKword(ListView):
    """lista de empleados por palabra clave """
    template_name = "persona/bykword.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        # variable para recoger la palabra que enviamos desde el form. con la instruccion request.GET le digo que me traiga todas
        # las solicitudes a servidor de tipo GET, cuyo identificador sea el kword, que es lo que le pusimos en el form en el html
        p_clave = self.request.GET.get("kword",'')
        #una vez que lo tengo lo puedo colocar en una lista como en el metodo anterior
        lista = Empleado.objects.filter(
            first_name = p_clave #en vez de definir el area de la empresa le pasamos el valor qaue tiene area. lo que recuperamos en la url
        )        
        return lista
        

#listar habilidades de empleados.
class ListHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        #aca le indicamos de cual empleado queremos traer las habilidades
        #en este caso por el empleado con el id numero 5, para hacerlo mas dinamos se puede utilizar la caja de texto del ejemplo mas arriba
        empleado = Empleado.objects.get(id=5)
        #con el metodo empleado.habilidades.all() es donde obtenemos todos las habilidades d eun empleado.
        #print(empleado.habilidades.all())

        return empleado.habilidades.all()

#listar empleados por trabajo
