# Generated by Django 4.2.5 on 2023-12-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='insta_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=255),
        ),
    ]
