from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_text = models.CharField(max_length=160)
    pub_date = models.DateTimeField('date published')
