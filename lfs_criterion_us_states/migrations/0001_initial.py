# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lfs_criterion_us_states.models


class Migration(migrations.Migration):

    dependencies = [
        ('criteria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='USStatesCriterion',
            fields=[
                ('criterion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='criteria.Criterion')),
                ('value', lfs_criterion_us_states.models.ListField()),
            ],
            bases=('criteria.criterion',),
        ),
    ]
