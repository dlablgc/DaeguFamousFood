from django.db import models

# Create your models here.

class Korean(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='korean/%Y/%m/%d', default='korean/no_image.png')
    
    desc = models.TextField()
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    
class China(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='china/%Y/%m/%d', default='china/no_image.png')
    
    desc = models.TextField()
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    def get__absolute_url(self):
        return self.title

class Western(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='western/%Y/%m/%d', default='western/no_image.png')
    
    desc = models.TextField()
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    def get__absolute_url(self):
        return self.title