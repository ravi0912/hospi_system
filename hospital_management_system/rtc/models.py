from django.db import models

# Create your models here.
# Anirudh Agnihotry
status_choice=(('0','Waiting'),('1','Pending'),('2','Completed'))
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

class Salt(models.Model):
	name = models.CharField(max_length=140)

	def __unicode__(self):
		return self.name

class Medicine(models.Model):
	name = models.CharField(max_length=140)
	salt = models.ManyToManyField('Salt')                                                                                                                                                             

	def __unicode__(self):
		return self.name



#Anirudh Agnihotry
