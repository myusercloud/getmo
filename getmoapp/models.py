from django.db import models

# Create your models here.
class patient(models.Model):
    fullname = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fullname

class doctors(models.Model):
    name = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    email = models.EmailField()
    status = models.CharField(max_length = 100)
    age = models.IntegerField()
    qualification = models.CharField(max_length = 100)

    def __str__(self):
        return self.name