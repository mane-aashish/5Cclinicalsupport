# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class clinicUserProfile(models.Model):
	uid = models.CharField(max_length = 50, primary_key=True)
	smokingHistory = models.CharField(max_length = 1, default="N")
	allergies = models.CharField(max_length = 50, blank=True, default="NIL")
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
	eosinophilia = models.CharField(max_length = 1, default="N")
	hiv = models.CharField(max_length = 1, default="N")
	mining = models.CharField(max_length = 1, default="N")

	def __unicode__(self):
		return self.uid


class radioUserProfileChest(models.Model):
	uid = models.CharField(max_length = 50, primary_key=True)
	honeycombing = models.CharField(max_length = 1, default="N")
	septal = models.CharField(max_length = 15, default="NULL")
	groundGlass = models.CharField(max_length = 15, default="NULL")
	consolidation = models.CharField(max_length = 25, default="NULL")
	fibrosis = models.CharField(max_length = 15, default="NULL")
	nodules = models.CharField(max_length = 15, default="NULL")
	massLesion = models.CharField(max_length = 1, default="N")
	treeInBudLesion = models.CharField(max_length = 1, default="N")
	airTrapping = models.CharField(max_length = 1, default="N")
	mosaicAttenuation = models.CharField(max_length = 1, default="N")
	bronchiectasis = models.CharField(max_length = 15, default="NULL")
	cavity = models.CharField(max_length = 15, default="NULL")
	cysts = models.CharField(max_length = 15, default="NULL")
	emphysema = models.CharField(max_length = 1, default="N")
	lymphNodes = models.CharField(max_length = 15, default="NULL")
	pleuralEffusion = models.CharField(max_length = 1, default="N")
	pleuralThickening = models.CharField(max_length = 15, default="NULL")
	crazyPaving = models.CharField(max_length = 1, default="N")
	haloSign = models.CharField(max_length = 1, default="N")
	reverseHalo = models.CharField(max_length = 1, default="N")
	fat = models.CharField(max_length = 1, default="N")
	heart = models.CharField(max_length = 15, default="NULL")

	def __unicode__(self):
		return self.uid


	

