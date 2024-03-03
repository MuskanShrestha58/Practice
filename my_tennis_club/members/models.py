from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        # esle garda hamro admin panel ma member haru herna khojda member ko nam dekhincha insteadof Member object(4) etc
        return f"{self.firstname} {self.lastname}"
