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



#create staff model
#firstname,lastname,position,tel,email,hiredate
#should return firstname and lastname


#create a ward model
#total beds, available beds
#return name


class staff(models.Model):
    fullnames = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    email = models.EmailField()
    tel = models.CharField(max_length = 100)
    hiredate = models.DateField()

    def __str__(self):
        return self.fullnames


class ward(models.Model):
    wardname = models.CharField(max_length = 100)
    totalbeds = models.CharField(max_length = 100)
    availablebeds = models.CharField(max_length = 100)

    def __str__(self):
        return self.wardname


class appointment1(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    date = models.DateField()
    department = models.CharField(max_length = 15)
    doctor = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name


class contactform(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    subject = models.CharField(max_length = 100)
    message = models.TextField()

    def __str__(self):
        return self.name