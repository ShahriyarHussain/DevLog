# Generated by Django 3.1.5 on 2021-03-14 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20210215_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_posted'],
            },
        ),
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('RESEARCH', 'Research'), ('TRAVEL', 'Travel'), ('ART', 'Art'), ('ASTROLOGY', 'Astrology'), ('PHOTO', 'Photo'), ('PROGRAMMING', 'Programming'), ('MISCALLENOUS', 'Miscallenous'), ('UPDATE', 'Update'), ('HOTFIX', 'Hotfix'), ('NATURE', 'Nature'), ('JOKE', 'Joke')], default='MISCALLENOUS', max_length=23),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]