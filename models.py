from django.db import models

class school_info(models.Model):
  #own info
	#
	school_id = models.IntegerField()
	#such as BUPT, UESTC
	school_name = models.CharField(max_length = 10)

class user_info(models.Model):
	#own info
	#
	userid = models.IntegerField()
	username = models.Charfield(max_length=20)
	email = models.CharField(max_length=50)
	gender = models.IntegerField() #0 for girl, 1 for boy
	preferred_lang = models.IntegerField()
	last_login = models.DateTimeField()
	
	#foreign keys
	#
	school_id = models.ForeignKey(School)

class user_auth(models.Model):
	#own info
	#
	passwd = models.CharField(max_length=100)
	#foreign keys
	#
	userid = models.ForeignKey(user_info)
	
