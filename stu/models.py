from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    birthday=models.DateField()

    def __str__(self) :
        
        return 'name:' + self.name + ';age:' + str(self.age) + ';birthday:' + str(self.birthday)
