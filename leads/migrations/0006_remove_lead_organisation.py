# Generated by Django 3.2.6 on 2021-08-13 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_lead_organisation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='organisation',
        ),
    ]
