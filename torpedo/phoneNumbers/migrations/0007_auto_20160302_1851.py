# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneNumbers', '0006_auto_20160301_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonenumbers',
            old_name='amnt_sent',
            new_name='amount_to_send',
        ),
    ]
