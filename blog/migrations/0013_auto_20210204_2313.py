# Generated by Django 3.1.5 on 2021-02-04 17:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20210204_2307'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment_table',
            new_name='Comments',
        ),
        migrations.RenameModel(
            old_name='Vote_table',
            new_name='Votes',
        ),
    ]