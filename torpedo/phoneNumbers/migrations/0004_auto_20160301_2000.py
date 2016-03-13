# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneNumbers', '0003_phonenumbers_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumbers',
            name='message',
            field=models.CharField(max_length=100),
        ),
    ]
