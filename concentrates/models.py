from django.db import models

class Concentrate(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='concentrates/img')

    def __str__(self):
        return self.name