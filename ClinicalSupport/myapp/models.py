# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class clinicUserProfile(models.Model):
	uid = models.CharField(max_length = 50)
	smokingHistory = models.BooleanField(default=False)
	allergies = models.CharField(max_length = 50, default="NULL")
	cough = models.BooleanField(default=False)
	fever = models.BooleanField(default=False)
	hemoptysis = models.BooleanField(default=False)
	breathlessness = models.BooleanField(default=False)
	skinrash = models.BooleanField(default=False)
	tb = models.BooleanField(default=False)
	cvd = models.BooleanField(default=False)
	sinusitis = models.BooleanField(default=False)
	asthma = models.BooleanField(default=False)
	dm = models.BooleanField(default=False)
	hiv = models.BooleanField(default=False)

	def __unicode__(self):
		return self.uid

	

