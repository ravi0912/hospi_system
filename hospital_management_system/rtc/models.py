from django.db import models

# Create your models here.
# Anirudh Agnihotry
status_choice=(('0','Waiting'),('1','Pending'),('2','Completed'))
rating=(('1','poor'),('2','Average'),('3','good'),('4','very good'),('5','excellent'))
category=(('1','poor'),('2','Average'),('3','good'),('4','very good'),('5','excellent'))
# Create your models here.
class CRequest(models.Model):
	name = models.CharField(max_length = 140)
	reg_no = models.CharField(max_length = 10, unique=True)
	problem= models.CharField(max_length = 140)
	submit_date = models.DateTimeField()
	appoint_date = models.DateTimeField()
	appoint_no = models.IntegerField(unique = True)
	#doctor = models.ForeignKey('Doctor')
	done = models.BooleanField(default = False)
	outsider = models.BooleanField(default= False)
	status =  models.CharField(max_length=1 ,choices=status_choice)
	
	def __unicode__(self):
		return self.name


class Medicine(models.Model):
	name = models.CharField(max_length=140)
	salt = models.TextField(blank=True) 
	mg = models.IntegerField()
	price = models.FloatField()
	disease = models.TextField(blank=True)
	misc = models.TextField(blank=True)
	prc = models.BooleanField()


	def __unicode__(self):
		return self.name



class FollowUp(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	rating = models.CharField(max_length=1,choices=rating)

	def __str__(self):
		return self.title

class Complaint(models.Model):
	username = models.CharField(max_length=140)
	category = models.CharField(max_length=10,choices=category)
	subject = models.CharField(max_length=140)
	complaint = models.TextField(blank=True)
	complaint_date = models.DateTimeField()
	doc_pat = models.BooleanField(default=0)

	def __str__(self):
		return self.subject




