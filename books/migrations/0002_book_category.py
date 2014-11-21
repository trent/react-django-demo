# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default='Fiction', max_length=50, choices=[(b'Autobiography', b'Autobiography'), (b'Biography', b'Biography'), (b'Fiction', b'Fiction'), (b'Non-Fiction', b'Non-Fiction'), (b'Play', b'Play')]),
            preserve_default=False,
        ),
    ]
