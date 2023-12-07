from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField(max_length=300)
    linkedin = models.URLField(max_length=300)
    bio = models.TextField()

    def __str__(self):
        return self.name
