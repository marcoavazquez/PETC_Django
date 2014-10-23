# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0002_ciclo_escuelasporciclo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('numero_grupos', models.PositiveIntegerField()),
                ('grado', models.PositiveIntegerField()),
                ('ciclo', models.ForeignKey(to='escuelas.Ciclo')),
                ('escuela', models.ForeignKey(to='escuelas.Escuela')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
