# Generated by Django 4.2.5 on 2023-12-10 05:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0003_userpofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPofile',
            new_name='UserProfile',
        ),
    ]
