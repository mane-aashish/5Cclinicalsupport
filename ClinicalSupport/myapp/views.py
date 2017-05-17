# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect, Http404
import string



# Importing models
from models import *


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
		patientDetails = {'smokingHistory': patientProfile.smokingHistory, 'allergies': patientProfile.allergies, 'cough': patientProfile.cough, 'fever': patientProfile.fever, 'hemoptysis':patientProfile.hemoptysis, 'breathlessness':patientProfile.breathlessness, 'skinrash':patientProfile.skinrash, 'tb':patientProfile.tb, 'cvd':patientProfile.cvd, 'sinusitis':patientProfile.sinusitis, 'asthma':patientProfile.asthma, 'dm':patientProfile.dm, 'hiv':patientProfile.hiv}
		return render(request, 'radio-chest.html',{'patientDetails': patientDetails})

	if request.method == 'POST':
		honeycombing = request.POST.get('honeycombing', 'N')
		septal = request.POST.get('septal', "NULL")
		groundGlass = request.POST.get('groundGlass', "NULL")
		consolidation = request.POST.get('consolidation', "NULL")
		fibrosis = request.POST.get('fibrosis', "NULL")
		nodules = request.POST.get('nodules', "NULL")
		massLesion = request.POST.get('massLesion', "N")
		treeInBudLesion = request.POST.get('treeInBudLesion', "N")
		airTrapping = request.POST.get('airTrapping', "N")
		mosaicAttenuation = request.POST.get('mosaicAttenuation', "N")
		bronchiectasis = request.POST.get('bronchiectasis', "NULL")
		cavity = request.POST.get('cavity', "NULL")
		cysts = request.POST.get('cysts', "NULL")
		emphysema = request.POST.get('emphysema', "N")
		lymphNodes = request.POST.get('lymphNodes', "NULL")
		pleuralEffusion = request.POST.get('pleuralEffusion', "N")
		pleuralThickening = request.POST.get('pleuralThickening', "NULL")
		crazyPaving = request.POST.get('crazyPaving', "N")
		haloSign = request.POST.get('haloSign', "N")
		reverseHalo = request.POST.get('reverseHalo', "N")
		fat = request.POST.get('fat', "N")
		heart = request.POST.get('heart', "NULL")
		uniqueID = request.session['radio-uid']

		userProfile = radioUserProfileChest.objects.create(uid=uniqueID, honeycombing=honeycombing, septal=septal, groundGlass=groundGlass, consolidation=consolidation, fibrosis=fibrosis, nodules=nodules, massLesion=massLesion, treeInBudLesion=treeInBudLesion, airTrapping=airTrapping, mosaicAttenuation=mosaicAttenuation, bronchiectasis=bronchiectasis, cavity=cavity, cysts=cysts, emphysema=emphysema, lymphNodes=lymphNodes, pleuralEffusion=pleuralEffusion, pleuralThickening=pleuralThickening, crazyPaving=crazyPaving, haloSign=haloSign, reverseHalo=reverseHalo, fat=fat, heart=heart)
		userProfile.save()

		response = render(request, "thanks.html")
		return response













	