from django.urls import reverse
from django.db import models
from django.conf import settings
# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img_path = models.TextField()
    class Meta:
        ordering = ('-pk',)
        
    #객체 표현
    def __str__(self):
        return self.img_path

