from django.db import models

# Create your models here.
class Student(models.Model):
        name = models.CharField(max_length=20)
        email = models.EmailField()
        gr_no = models.IntegerField()
        branch = models.CharField(max_length=10)
        year = models.CharField(max_length=12)
        query = models.CharField(max_length=200)
        date = models.DateTimeField()

        def __str__(self):
            return self.name
        

