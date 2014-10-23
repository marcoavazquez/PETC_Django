# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0002_ciclo_escuelasporciclo'),
        ('personal', '0002_auto_20141022_0443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apoyo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bruto_mensual', models.DecimalField(max_digits=8, decimal_places=2)),
                ('isr_mensual', models.DecimalField(max_digits=8, decimal_places=2)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('ciclo', models.ForeignKey(to='escuelas.Ciclo')),
                ('rfc_personal', models.ForeignKey(to='personal.Personal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
