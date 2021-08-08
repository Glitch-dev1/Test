from django.db import models

# Create your models here.


class Article(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to="media",null=True)
    
    class Meta:
      db_table = "gallery"
      
    def get_obsolute_url(self):
        
        return f"/blog/{self.id}"
        
class SendEmail(models.Model):
  subject = models.CharField(max_length=50)
  message = models.TextField()
  email = models.EmailField()
