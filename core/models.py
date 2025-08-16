from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title