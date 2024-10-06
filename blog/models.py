from email.mime import image
from operator import truediv
from pyexpat import model
import re
from turtle import mode
from unicodedata import category
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
    

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title =  models.CharField(max_length=200)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.post.title}"