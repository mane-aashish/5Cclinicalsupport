# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.template import Context
from django.http import HttpResponse



# Importing models
from models import clinicUserProfile

# Universal ID
uid = 0;

# Create your views here.
def startup(request, rid):
	response = render(request, "clinic.html")
	request.session['uid'] = rid
	print "UID = " + request.session['uid']
	return response

def storeClinicInfo(request):
	
	if request.method == 'POST':
		smokingHistory = request.POST.get('smoking', 'N')
		allergies = request.POST['allergies']
		cough = request.POST.get('cough', 'N')
		fever = request.POST.get('fever', 'N')
		hemoptysis = request.POST.get('hemoptysis','N')
		breathlessness = request.POST.get('breathlessness','N')
		skinrash = request.POST.get('skinrash','N')
		tb = request.POST.get('tb', 'N')
		cvd = request.POST.get('cvd', 'N')
		sinusitis = request.POST.get('sinusitis', 'N')
		asthma = request.POST.get('asthma', 'N')
		dm = request.POST.get('dm', 'N')
		hiv = request.POST.get('hiv', 'N')
		uniqueID = str(request.session['uid'])
		print "Unique ID = " + uniqueID

		userProfile = clinicUserProfile.objects.create(uid=uniqueID, smokingHistory=smokingHistory, allergies=allergies, cough=cough, fever=fever, hemoptysis=hemoptysis, breathlessness=breathlessness, skinrash=skinrash, tb=tb, cvd=cvd, sinusitis=sinusitis, asthma=asthma, dm=dm, hiv=hiv)
		userProfile.save()

		response = render(request, "thanks.html")
		return response




	