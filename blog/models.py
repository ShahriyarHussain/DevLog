from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField


POST_TYPES = [
    ('RESEARCH', 'Research'),
    ('TRAVEL', 'Travel'),
    ('ART', 'Art'),
    ('ASTROLOGY', 'Astrology'),
    ('PHOTO', 'Photo'),
    ('PROGRAMMING', 'Programming'),
    ('MISCELLANEOUS', 'Miscellaneous'),
    ('UPDATE', 'Update'),
    ('HOTFIX', 'Hotfix'),
    ('NATURE', 'Nature'),
    ('JOKE', 'Joke')
]


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = ResizedImageField(
        size=[620, 500], upload_to='post_images', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_type = models.CharField(
        default='MISCELLANEOUS', max_length=23, choices=POST_TYPES)

    def __self__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Votes(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'author'], name='pk_vote')]

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.BooleanField()

    def __self__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_posted']

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.id})

    def __self__(self):
        return self.title
