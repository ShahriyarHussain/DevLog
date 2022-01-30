# Generated by Django 3.1.5 on 2021-02-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('RESEARCH', 'Research'), ('TRAVEL', 'Travel'), ('ART', 'Art'), ('ASTROLOGY', 'Astrology'), ('PHOTO', 'Photo'), ('PROGRAMMING', 'Programming'), ('MISCELLANEOUS', 'Miscellaneous'), ('UPDATE', 'Update'), ('HOTFIX', 'Hotfix'), ('NATURE', 'Nature'), ('JOKE', 'Joke')], default='MISCELLANEOUS', max_length=23),
        ),
    ]