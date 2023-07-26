from django.db import models
import datetime

# Create your models here.
class BlogPost(models.Model):
    
    model_id = models.AutoField(primary_key=True)
    model_title = models.CharField(max_length=500)
    model_author = models.CharField(max_length=150)
    model_short = models.CharField(max_length=1500)
    model_post = models.CharField(max_length=10000, default="Not Added")
    model_like = models.IntegerField(default=0)
    model_cat = models.CharField(max_length=25, default="Tehnology")
    last_visit = models.DateTimeField(auto_now_add=True)
    view_counter = models.IntegerField(default=0)

    
    
    def __str__(self):
        return self.model_title

