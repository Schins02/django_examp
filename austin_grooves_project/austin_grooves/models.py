from django.db import models

# Create your models here.

class User(models.Model) :
	name = models.CharField(max_length = 20, unique = True)

	def __unicode__(self) :
		return self.name

class Band(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length = 128)

	def __unicode__(self) :
		return self.title






