# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
        ('caracteristicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave', models.CharField(unique=True, max_length=15)),
                ('nombre', models.CharField(max_length=100)),
                ('zona', models.PositiveIntegerField()),
                ('sector', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('telefono', models.CharField(max_length=25)),
                ('calle', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=30)),
                ('colonia', models.CharField(max_length=255)),
                ('cod_postal', models.PositiveIntegerField()),
                ('afiliada', models.BooleanField(default=False)),
                ('localidad', models.ForeignKey(to='lugares.Localidad')),
                ('modalidad', models.ForeignKey(to='caracteristicas.Modalidad')),
                ('municipio', models.ForeignKey(to='lugares.Municipio')),
                ('nivel', models.ForeignKey(to='caracteristicas.Nivel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
