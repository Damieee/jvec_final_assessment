from django.db import models

class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Comment(models.Model):
    news_item = models.CharField(max_length=255)
    text = models.TextField()
