from typing import Type
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.options import Options
from django.template.defaultfilters import slugify
from django.urls import reverse


User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    created_on = models.DateField(blank=True, null=True)
    published_on = models.BooleanField(default=False, verbose_name="published")
    content = models.TextField(blank=True, verbose_name="content")
    thumbnail = models.ImageField(blank=True, upload_to= 'blog')


    class Meta:
        ordering = ['-created_on']
        verbose_name = "Blog Post"


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        super().save(*args, **kwargs)


    @property
    def author_default(self):
        return self.author.username if self.author else "Unknown author"

    def get_absolute_url(self):
        return reverse('posts:home')