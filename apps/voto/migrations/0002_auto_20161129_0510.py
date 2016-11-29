# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='categoria',
            field=models.ForeignKey(to='voto.Categoria'),
        ),
    ]
