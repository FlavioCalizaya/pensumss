# Generated by Django 3.2.4 on 2022-09-24 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('total_materias', models.IntegerField(verbose_name=11)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('prerrequisito', models.CharField(max_length=50)),
                ('semestre', models.IntegerField(verbose_name=2)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Materia_Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=50)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.docente')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.materia')),
            ],
        ),
        migrations.AddField(
            model_name='docente',
            name='materia',
            field=models.ManyToManyField(through='api.Materia_Docente', to='api.Materia'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.facultad'),
        ),
    ]
