from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 200)
	publisher = models.CharField(max_length = 200)
	description = models.CharField(max_length = 2000) 
	genre = models.CharField(max_length = 50) 
	pub_date = models.DateField() 
	ISBN = models.CharField(max_length = 20) 
	edition = models.CharField(max_length = 30)

	def __str__(self):
		return self.title + ',' + self.author	 

class Review(models.Model):
	book = models.ForeignKey(Book)
	text = models.CharField(max_length = 1000)	
	user = models.ForeignKey(User,default='1')
	
	def __str__(self):
		return self.book.title + ':' + self.text	 
