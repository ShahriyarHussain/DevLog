from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from PIL import Image

POST_TYPES = [
    ('RESEARCH', 'Research'),
    ('TRAVEL', 'Travel'),
    ('ART', 'Art'),
    ('ASTROLOGY', 'Astrology'),
    ('PHOTO', 'Photo'),
    ('PROGRAMMING', 'Programming'),
    ('MISCALLENOUS', 'Miscallenous'),
    ('UPDATE', 'Update'),
    ('HOTFIX', 'Hotfix'),
    ('NATURE', 'Nature'),
    ('JOKE', 'Joke')
]


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    image = ResizedImageField(
        size=[620, 500], upload_to='post_images', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_type = models.CharField(
        default='MISCALLENOUS', max_length=23, choices=POST_TYPES)
    # vote = models.OneToOneField(pk_vote, on_delete=models.CASCADE)

    def __self__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Vote(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'author'], name='pk_vote')]

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.BooleanField()

    def __self__(self):
        return self.author


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField()
    time_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_posted']

    def __self__(self):
        return self.author
