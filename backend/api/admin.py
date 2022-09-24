from django.contrib import admin
from .models import Materia, Carrera, Facultad, Docente, Materia_Docente

# Register your models here.
admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Materia)
admin.site.register(Docente)
admin.site.register(Materia_Docente)
