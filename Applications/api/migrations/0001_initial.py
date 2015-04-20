# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('duration', models.CharField(max_length=10)),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileContributer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('label', models.CharField(max_length=30, db_index=True)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=7, db_index=True)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=7, db_index=True)),
                ('img', django_base64field.fields.Base64Field(blank=True, null=True, max_length=255, default='')),
                ('postal_address', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('availibility', models.TextField()),
                ('contact', models.TextField()),
                ('visible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileVisitor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('labels_interested_in', models.TextField()),
                ('img', django_base64field.fields.Base64Field(blank=True, null=True, max_length=255, default='')),
                ('id_bid', models.PositiveIntegerField()),
                ('favorite', models.ManyToManyField(to='api.ProfileContributer')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('label', models.CharField(max_length=50, db_index=True)),
                ('tagged', models.ManyToManyField(to='api.ProfileVisitor')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('registration_history', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profilevisitor',
            name='id_user',
            field=models.OneToOneField(to='api.UserProfile'),
        ),
        migrations.AddField(
            model_name='profilecontributer',
            name='id_user',
            field=models.OneToOneField(to='api.UserProfile'),
        ),
        migrations.AddField(
            model_name='bid',
            name='id_Contributer',
            field=models.OneToOneField(blank=True, null=True, to='api.ProfileContributer'),
        ),
        migrations.AddField(
            model_name='bid',
            name='id_user',
            field=models.OneToOneField(blank=True, null=True, to='api.UserProfile'),
        ),
    ]
