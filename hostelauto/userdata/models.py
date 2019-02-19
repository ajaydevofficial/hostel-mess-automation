from django.db import models

# Create your models here.
class userdata(models.Model):

    name = models.CharField(max_length=50)
    bill = models.DecimalField(max_digits=50,decimal_places = 5)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
