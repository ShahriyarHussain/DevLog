# Generated by Django 3.1.5 on 2021-08-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210321_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('ACADEMIC', 'Academic'), ('TRAVEL', 'Travel'), ('ART', 'Art'), ('SCIENCE', 'Science'), ('PROGRAMMING', 'Programming'), ('MISCALLENOUS', 'Miscallenous'), ('UPDATE', 'Update'), ('MOVIES', 'Movies'), ('TRENDING', 'Trending')], default='MISCALLENOUS', max_length=23),
        ),
    ]
