# Generated by Django 3.1.5 on 2021-02-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('RESEARCH', 'Research'), ('TRAVEL', 'Travel'), ('ART', 'Art'), ('ASTROLOGY', 'Astrology'), ('PHOTO', 'Photo'), ('PROGRAMMING', 'Programming'), ('MISCALLENOUS', 'Miscallenous'), ('UPDATE', 'Update'), ('HOTFIX', 'Hotfix'), ('NATURE', 'Nature'), ('JOKE', 'Joke')], default='MISCALLENOUS', max_length=23),
        ),
    ]
