from django.db import models

# Create your models here.
class Instrument(models.Model):
	cover = models.ImageField(upload_to='images/')
	types=models.CharField(max_length=50)
	manufacturer=models.CharField(max_length=50)
	isonbase=models.BooleanField(default=False)
	medonbox=models.BooleanField(default=False)
	caponbox=models.BooleanField(default=False)
	stronbox=models.BooleanField(default=False)


