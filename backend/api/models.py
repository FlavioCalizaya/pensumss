from django.db import models
# Create your models here.

class Facultad(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    

class Carrera(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    facultad = models.ForeignKey(Facultad, on_delete = models.CASCADE, null=False, blank = False)
    total_materias = models.IntegerField(11)


class Materia(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete = models.CASCADE, null=False, blank = False)
    prerrequisito = models.CharField(max_length=50)
    semestre =  models.IntegerField(2)


class Docente(models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    materia = models.ManyToManyField(Materia, through = 'Materia_Docente')


class Materia_Docente(models.Model):
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE, null=False, blank = False)
    docente = models.ForeignKey(Docente, on_delete = models.CASCADE, null=False, blank = False)
    grupo = models.CharField(max_length=50)
 
 