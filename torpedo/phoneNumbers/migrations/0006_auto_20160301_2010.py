# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneNumbers', '0005_phonenumbers_amnt_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumbers',
            name='amnt_sent',
            field=models.CharField(max_length=10),
        ),
    ]
