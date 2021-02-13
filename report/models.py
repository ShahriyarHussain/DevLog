from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)

    def __self__(self):
        return self.title
