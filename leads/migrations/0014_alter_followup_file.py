# Generated by Django 3.2.6 on 2021-08-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0013_followup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
