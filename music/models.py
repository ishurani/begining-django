from django.db import models

# Create your models here.
class Topic(models.Model):
    number = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    amount = models.IntegerField()
    price = models.IntegerField(default=100)
   
    def __str__(self):
        return self.number

class webpage(models.Model):
    topic=models.CharField(max_length=100,unique='True')
    name=models.CharField(max_length=100,unique='True')
    url=models.URLField(max_length=100,unique='True')

    def __str__(self):
        return self.number
