
from __future__ import unicode_literals

from django.db import models

def user_directory_path(instance, filename):
	return 'Client/'+ instance.name+'.jpg'

class Person(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	phone=models.CharField(max_length=100)
	file=models.FileField(max_length=100,upload_to=user_directory_path)
	ip_addr = models.CharField(max_length=20, default='')
	country=models.CharField(max_length=100, default='')
	country_code=models.CharField(max_length=100, default='')
	city=models.CharField(max_length=100, default='')
	city_postal_code=models.CharField(max_length=100, default='')
	latitude=models.CharField(max_length=100, default='')
	longitude=models.CharField(max_length=100, default='')
	dma_code=models.CharField(max_length=100, default='')
	def __str__(self):
		return self.name