from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    """
    Model for blog post categories.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Model for a blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to access a detail record for this post.
        """
        return reverse('post_detail', args=[str(self.id)])
