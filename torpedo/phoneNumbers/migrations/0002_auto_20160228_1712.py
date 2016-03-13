# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneNumbers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonenumbers',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
    ]
