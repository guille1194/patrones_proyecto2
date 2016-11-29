# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('ID_Categoria', models.AutoField(serialize=False, primary_key=True)),
                ('num_cat', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Opcion_Pregunta',
            fields=[
                ('ID_Opcion_Pregunta', models.AutoField(serialize=False, primary_key=True)),
                ('opcion', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('ID_Pregunta', models.AutoField(serialize=False, primary_key=True)),
                ('tipo', models.BooleanField(default=False)),
                ('pregunta', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=64)),
                ('fecha_creacion', models.DateField(default=datetime.date.today)),
                ('publicado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('ID_Respuesta', models.AutoField(serialize=False, primary_key=True)),
                ('respuesta', models.CharField(max_length=200)),
                ('ID_Pregunta', models.ForeignKey(to='voto.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta_Opcion',
            fields=[
                ('ID_Respuesta_Opcion', models.AutoField(serialize=False, primary_key=True)),
                ('ID_Opcion_Pregunta', models.ForeignKey(to='voto.Opcion_Pregunta')),
                ('ID_Respuesta', models.ForeignKey(to='voto.Respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('ID_Usuario', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('user_perfil', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='respuesta',
            name='ID_Usuario',
            field=models.ForeignKey(to='voto.Usuario'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='ID_Usuario',
            field=models.ForeignKey(to='voto.Usuario'),
        ),
        migrations.AddField(
            model_name='opcion_pregunta',
            name='ID_Pregunta',
            field=models.ForeignKey(to='voto.Pregunta'),
        ),
    ]
