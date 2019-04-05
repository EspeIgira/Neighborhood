from django.db import models


class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30,blank=True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
