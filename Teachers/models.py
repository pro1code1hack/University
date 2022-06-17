from django.db import models


# Create your models here.

class Person(models.Model):  # все модели джанго наследуются от models.Model
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name




class Teacher(Person, models.Model):
    salary = models.IntegerField()
    # articles = models.ManyToManyField('Article')  #TODO dodelat
    educational_institution = models.CharField(max_length=50)
    work_experiences = models.CharField(max_length=1000)
    subject = models.CharField(max_length=50, null=True, default="Physcis")
    # responses = models.ManyToManyField('Response')
