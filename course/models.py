from email.policy import default
from django.db import models
from django.utils import timezone
from users.models import User
from django.core.validators import FileExtensionValidator

class course(models.Model):
    title = models.CharField(max_length=50)
    alt = models.TextField(null=True, blank=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='img_uploaded', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title