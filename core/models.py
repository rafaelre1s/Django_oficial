from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=(('draft', 'Rascunho'), ('published', 'Publicado')),
        default='draft'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title