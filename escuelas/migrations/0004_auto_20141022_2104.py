# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0003_auto_20141022_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciclo',
            name='ciclo',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
