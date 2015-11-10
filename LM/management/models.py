from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

class MyUser(models.Model):
	user = models.OneToOneField(User)
	nickname = models.CharField(max_length = 16)
	permission = models.IntegerField()

	def __unicode__(self):
		return self.user.username

class Book(models.Model):
	name = models.CharField(max_length = 128)
	price = models.FloatField()
	author = models.CharField(max_length = 128)
	pubDate = models.DateField()
	typ = models.CharField(max_length = 128)
    

	class META:
		ordering = ['name']

	def __unicode__(self):
		return self.name


class Img(models.Model):
	name = models.CharField(max_length = 128)
	desc = models.TextField()
	img = models.ImageField(upload_to = 'image')
	book = models.ForeignKey(Book)
    
	class META:
		ordering = ['name']

	def __unicode__(self):
		return self.name

class Reservation(models.Model):
    book=models.ForeignKey(Book)
    user=models.ForeignKey(MyUser)
    resDate=models.DateField()
    def __unicode__(self):
        return self.book.name

class BookT(models.Model):
    book=models.ForeignKey(Book)
    avail = models.BooleanField(default=True)
    desc = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=200)
    borrowPeriod= models.DurationField()
    publisher = models.CharField(max_length=128, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
       return self.book.name

class BorrowInfo(models.Model):
    book=models.ForeignKey(Book)
    user=models.ForeignKey(MyUser)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True,blank=True)
    def __unicode__(self):
        return self.book.name

class BookEval(models.Model):
    book=models.ForeignKey(Book)
    user=models.ForeignKey(MyUser)
    Excellent = 'ex'
    Good = 'go'
    Average = 'av'
    Fair = 'fa'
    Poor = 'po'
    RATE_CHOICE = (
                   (Excellent,'Excellent'),
                   (Good,'Good'),
                   (Average,'Average'),
                   (Fair,'Fair'),
                   (Poor,'Poor'),
                   )
    rate = models.CharField(max_length=2,choices=RATE_CHOICE,default=Excellent)
    def __unicode__(self):
        return self.book.name





