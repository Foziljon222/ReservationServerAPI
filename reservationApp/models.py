from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Restourant(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=255)
    description = models.TextField()
    def str(self):
        return self.name


class Table(models.Model):
    restourant = models.ForeignKey(Restourant,related_name='tables',on_delete=models.CASCADE)
    number = models.IntegerField()
    capacity = models.IntegerField()

    def str(self):
        return f'Table {self.number} at {self.restourant.name}'


class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    table = models.ForeignKey(Table,on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()

    def str(self):
        return f'{self.user.username} reserved {self.table} at {self.reservation_time}'