from django.db import models

class Point(models.Model):
  title = models.CharField(max_length=100)
  lat = models.FloatField()
  lng = models.FloatField()
  food = models.CharField(max_length=100, null=True)
  booze = models.CharField(max_length=100, null=True)
  kakaourl = models.CharField(max_length=100, null=True)

  def __str__(self):
    return '%s %s %s' % (self.id, self.title, self.food)