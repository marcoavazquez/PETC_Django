# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0002_ciclo_escuelasporciclo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='escuelasporciclo',
            unique_together=set([('ciclo', 'escuela')]),
        ),
    ]
