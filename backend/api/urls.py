from unicodedata import name
from django.urls import path
from .views import MateriaView, DocenteView

urlpatterns = [
    path('materias/',MateriaView.as_view(), name='materias_list'),
    path('docentes/',DocenteView.as_view(), name='docentes_list')
]