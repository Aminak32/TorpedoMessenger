# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneNumbers', '0002_auto_20160228_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumbers',
            name='message',
            field=models.CharField(default=b'None', max_length=100),
        ),
    ]
