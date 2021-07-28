from django.db import models

# Create your models here.


class Article(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()
    
    def get_obsolute_url(self):
        
        return f"/blog/{self.id}"