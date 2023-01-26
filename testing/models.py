from django.db import models

class movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testing/static/assets/images')
    def __str__(self):
        return self.title
