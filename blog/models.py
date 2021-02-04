from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __self__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Vote_table(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'author'], name='pk_vote')]
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.BooleanField()

    def __self__(self):
        return self.title


class Comment_table(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'author'], name='pk_comment')]
    # class Meta:
    #     unique_together = (('post', 'author'),)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    time_posted = models.DateTimeField(default=timezone.now)

    def __self__(self):
        return self.title
