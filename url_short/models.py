from django.db import models
import datetime

class URL(models.Model):  
    full_url = models.URLField(unique=True)   
    created = models.DateTimeField(default=datetime.datetime.now(), editable=False)    

    def __str__(self):
        return self.full_url
