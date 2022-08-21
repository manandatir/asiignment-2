from django.db import models

# Create your models here.
class  Student(models.Model):
    name=models.CharField(max_length=100)
    des=models.TextField()
    def _str_(self):
        return  self.name