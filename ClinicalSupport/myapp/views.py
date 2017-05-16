# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.template import Context
from django.http import HttpResponse



# Importing models
from models import clinicUserProfile

# Create your views here.
def startup(request, uid):
	response = render(request, "clinic.html")
	return response

def storeClinicInfo(request):
	
	if request.method == 'GET':
		response = render(request, "clinic.html")
		return response


	if request.method == 'POST':
		uid = "123456"
		smokingHistory = request.POST['smoking']
		allergies = request.POST['allergies']
		cough = request.POST['cough']
		fever = request.POST['fever']
		hemoptysis = request.POST['hemoptysis']
		breathlessness = request.POST['breathlessness']
		skinrash = request.POST['skinrash']
		tb = request.POST['tb']
		cvd = request.POST['cvd']
		sinusitis = request.POST['sinusitis']
		asthma = request.POST['asthma']
		dm = request.POST['dm']

		userProfile = clinicUserProfile.objects.create(uid=uid, smokingHistory=smokingHistory, allergies=allergies, cough=cough, fever=fever, hemoptysis=hemoptysis, breathlessness=breathlessness, skinrash=skinrash, tb=tb, cvd=cvd, sinusitis=sinusitis, asthma=asthma, dm=dm, hiv=hiv)
		userProfile.save()




	