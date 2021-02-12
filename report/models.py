from django.db import models


class Feedback(models.Model):
    email = models.EmailField(max_length=254, blank=True, null=True)
    name = models.CharField(default='Anonymous', max_length=100)
    content = models.TextField()

    def __self__(self):
        return self.title
