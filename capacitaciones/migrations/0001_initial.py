# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0002_ciclo_escuelasporciclo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capacitacion', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CapacitacionesPorEscuela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('capacitacion', models.ForeignKey(to='capacitaciones.Capacitacion')),
                ('clave_escuela', models.ForeignKey(to='escuelas.Escuela')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
