# Generated by Django 4.2.13 on 2024-05-22 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=50)),
                ('profile_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(default=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=255)),
                ('bio', models.TextField(blank=True, default='')),
                ('city', models.CharField(blank=True, default='', max_length=255)),
                ('country', models.CharField(blank=True, default='', max_length=255)),
                ('occupation', models.CharField(blank=True, default='', max_length=255)),
                ('organization', models.CharField(blank=True, default='', max_length=255)),
                ('skills', models.CharField(blank=True, default='', max_length=255)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('social_links', models.ManyToManyField(blank=True, to='userprofiles.sociallink')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sociallink',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofiles.userprofile'),
        ),
    ]
