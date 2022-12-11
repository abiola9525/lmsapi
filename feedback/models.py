import email
from django.db import models

class feed(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
