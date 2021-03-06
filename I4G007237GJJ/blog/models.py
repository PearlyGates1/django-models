from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, help_text='Enter field documentation')
    text = models.TextField()
    author = models.ForeignKey(on_delete=models.CASCADE,
    related_name='blog_posts')
    created_date = models.DateTimeField(auto_now_add=True)
    publshed_date = models.DateTimeField()
