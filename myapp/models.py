from django.db import models

class MyappConfig(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' ' + self.value