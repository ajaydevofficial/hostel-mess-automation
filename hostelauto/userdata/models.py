from django.db import models

# Create your models here.
class userdata(models.Model):

    name = models.CharField(max_length=50)
    morning = models.CharField(max_length=50,null=True,default=0)
    lunch = models.CharField(max_length=50,null=True,default=0)
    evening = models.CharField(max_length=50,null=True,default=0)
    bill = models.DecimalField(max_digits=50,decimal_places = 5)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
