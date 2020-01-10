from django.db import models


class job(models.Model):
    imagefun = models.ImageField(upload_to='images/')
    summery = models.CharField(max_length=200)