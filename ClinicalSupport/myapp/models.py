# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class clinicUserProfile(models.Model):
	uid = models.CharField(max_length = 50, primary_key=True)
	smokingHistory = models.CharField(max_length = 1, default="N")
	allergies = models.CharField(max_length = 50, blank=True)
	cough = models.CharField(max_length = 1, default="N")
	fever = models.CharField(max_length = 1, default="N")
	hemoptysis = models.CharField(max_length = 1, default="N")
	breathlessness = models.CharField(max_length = 1, default="N")
	skinrash = models.CharField(max_length = 1, default="N")
	tb = models.CharField(max_length = 1, default="N")
	cvd = models.CharField(max_length = 1, default="N")
	sinusitis = models.CharField(max_length = 1, default="N")
	asthma = models.CharField(max_length = 1, default="N")
	dm = models.CharField(max_length = 1, default="N")
	hiv = models.CharField(max_length = 1, default="N")

	def __unicode__(self):
		return self.uid

	

