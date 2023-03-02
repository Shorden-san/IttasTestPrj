from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def all_phones_row(self):
        return ", ".join([number.number for number in self.phones.all()])


class Phone(models.Model):
    number = models.CharField(max_length=16) #+375 37 5375375
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, default=0, related_name="phones")

    def __str__(self):
        return self.number