# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20141022_0443'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='personalporciclo',
            unique_together=set([('personal', 'ciclo', 'escuela')]),
        ),
    ]
