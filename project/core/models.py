from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    class Meta:
        get_latest_by = 'date_posted'
    def __str__(self):
        return self.title

class Trip(models.Model):
    country = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='trip_images/', blank=True, null=True)
    
    def __str__(self):
        return self.country
