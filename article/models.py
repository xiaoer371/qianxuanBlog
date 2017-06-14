# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	"""docstring for ClassName"""
	title = models.CharField(max_length = 100)
	category = models.CharField(max_length = 50, blank = True)
	date_time = models.DateTimeField(auto_now_add = True)
	content = models.TextField(blank = True, null = True)
	# python2 use __unicode__, python3 use __str__
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-date_time'] 
