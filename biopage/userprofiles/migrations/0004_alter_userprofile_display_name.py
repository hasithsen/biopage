# Generated by Django 4.2.13 on 2024-05-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_alter_userprofile_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='display_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
