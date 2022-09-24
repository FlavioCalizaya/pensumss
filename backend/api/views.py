from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Materia, Docente
import json

# Create your views here.
class MateriaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    def get(self, request, id=0):
        if (id > 0):
            materias = list(Materia.objects.filter(id=id).values())
            if len(materias) > 0:
                materia = materias[0]
                datos = {'message': "Success", 'materia': materia}
            else:
                datos = {'message': "materia not found..."}
            return JsonResponse(datos)
        else:
            materias = list(Materia.objects.values())
            if len(materias) > 0:
                datos = {'message': "Success", 'materias': materias}
            else:
                datos = {'message': "materias not found..."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Materia.objects.create(codigo=jd['codigo'], nombre=jd['nombre'], id_carrera=jd['id_carrera'], prerrequisito=jd['prerrequisito'], semestre=jd['semestre'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        materias = list(Materia.objects.filter(id=id).values())
        if len(materias) > 0:
            materia = Materia.objects.get(id=id)
            materia.codigo = jd['codigo']
            materia.nombre = jd['nombre']
            materia.id_carrera = jd['id_carrera']
            materia.prerrequisito = jd['prerrequisito']
            materia.semestre = jd['semestre']
            materia.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Materia not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        materias = list(Materia.objects.filter(id=id).values())
        if len(materias) > 0:
            Materia.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Materia not found..."}
        return JsonResponse(datos)


class DocenteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    def get(self, request, id=0):
        if (id > 0):
            docentes = list(Docente.objects.filter(id=id).values())
            if len(docentes) > 0:
                docente = docentes[0]
                datos = {'message': "Success", 'docente': docente}
            else:
                datos = {'message': "docente not found..."}
            return JsonResponse(datos)
        else:
            docentes = list(Docente.objects.values())
            if len(docentes) > 0:
                datos = {'message': "Success", 'docentes': docentes}
            else:
                datos = {'message': "docentes not found..."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Docente.objects.create(codigo=jd['codigo'], nombre=jd['nombre'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        docentes = list(Docente.objects.filter(id=id).values())
        if len(docentes) > 0:
            docente = Docente.objects.get(id=id)
            docente.codigo = jd['codigo']
            docente.nombre = jd['nombre']
            docente.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Docente not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        docentes = list(Docente.objects.filter(id=id).values())
        if len(docentes) > 0:
            Docente.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Docente not found..."}
        return JsonResponse(datos)

