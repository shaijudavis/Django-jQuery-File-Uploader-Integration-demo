from django.db import models

class Image(models.Model):
    filename = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
                                    
    def __unicode__(self):
       return self.filename
        
