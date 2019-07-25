# Generated by Django 2.1.7 on 2019-07-25 03:38

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0002_jsonfileupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_id', models.CharField(max_length=16)),
                ('campaign_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='jsondatamodel',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
