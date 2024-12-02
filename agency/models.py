from django.db import models
from django.contrib.auth.models import AbstractUser


class Cat(AbstractUser):
    name = models.CharField(max_length=63)
    experience = models.IntegerField(default=0)
    breed = models.CharField(max_length=63)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.name}({self.breed})"


class Target(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)
    notes = models.TextField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}({self.country})"


class Mission(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    target = models.ManyToManyField(Target)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cat} - {self.target}({self.complete})"
