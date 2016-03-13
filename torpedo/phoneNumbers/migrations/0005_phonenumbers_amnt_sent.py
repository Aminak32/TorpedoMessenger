# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneNumbers', '0004_auto_20160301_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumbers',
            name='amnt_sent',
            field=models.CharField(default=b'None', max_length=10),
        ),
    ]
