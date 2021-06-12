from django.db import models

# Create your models here.
class Student(models.Model):
        name = models.CharField(max_length=20)
        token = models.IntegerField(default=0)
        email = models.EmailField()
        gr_no = models.IntegerField()
        branch = models.CharField(max_length=10)
        year = models.CharField(max_length=12)
        query = models.CharField(max_length=200, null=True, blank=True)
        date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name

class Alumni(models.Model):
    name = models.CharField(max_length=20)
    token = models.IntegerField(default=0)
    email = models.EmailField()
    gr_no = models.IntegerField()
    branch = models.CharField(max_length=10)
    query = models.CharField(max_length=200, null=True, blank=True)
    passout = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

        
class CurrentToken(models.Model):
    token = models.IntegerField(default=0)

    def __str__(self):
        return str(self.token)

class AlumniCurrentToken(models.Model):
    token = models.IntegerField(default=0)

    def __str__(self):
        return str(self.token)
    

