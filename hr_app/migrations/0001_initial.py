# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Honor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(default=2014, max_length=5)),
                ('award_level', models.CharField(max_length=50, choices=[(b'Honor', b'More than 50 Hours'), (b'High', b'More than 100 Hours')])),
                ('bar_status', models.CharField(max_length=200, choices=[(b'Active', b'Licensed to Practice Law in the District'), (b'Other State', b'Licensed to Practice Law in another Jurisdiction')])),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Honoree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization_name', models.CharField(max_length=200)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name=b'children', blank=True, to='hr_app.Organization', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='honoree',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name=b'lawyers', to='hr_app.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='honor',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name=b'honors', to='hr_app.Honoree'),
            preserve_default=True,
        ),
    ]
