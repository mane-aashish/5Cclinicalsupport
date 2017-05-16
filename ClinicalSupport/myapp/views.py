# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect, Http404
import string



# Importing models
from models import clinicUserProfile


# Create your views here.


# This view is used to capture the UID and store the clinicInfo 
def storeClinicInfo(request, rid):

	if request.method == 'GET':
		request.session['uid'] = str(rid)
		return render(request, "clinic.html")

	
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
		uniqueID = request.session['uid']

		userProfile = clinicUserProfile.objects.create(uid=uniqueID, smokingHistory=smokingHistory, allergies=allergies, cough=cough, fever=fever, hemoptysis=hemoptysis, breathlessness=breathlessness, skinrash=skinrash, tb=tb, cvd=cvd, sinusitis=sinusitis, asthma=asthma, dm=dm, hiv=hiv)
		userProfile.save()

		response = render(request, "thanks.html")
		return response

def viewChestClinicInfo(request, rid):
	
	if request.method == 'GET':
		request.session['radio-uid'] = str(rid)
		patientProfile = clinicUserProfile.objects.get(uid=request.session['radio-uid'])	
		patientDetails = {'smokingHistory': patientProfile.smokingHistory, 'allergies': patientProfile.allergies, 'cough': patientProfile.cough, 'fever': patientProfile.fever}
		return render(request, 'radio-chest.html',{'patientDetails': patientDetails})




	