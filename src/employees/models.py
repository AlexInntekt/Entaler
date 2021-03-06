from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=35)
    about = models.TextField(default='')
    age = models.IntegerField()
    image = models.ImageField(upload_to='postImage', blank=True)

    def __str__(self):
        return self.name