# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
import string



# Importing models
from models import *


""" Creating the observation - disease dictionary mapping

	Entries should be in the form Disease: Symptoms """

diseaseDict = {
	"UIP": "Honeycombing; Fibrosis-Basal",
	"NSIP": "Septal Thickening-Irregular; Fibrosis-Mixed; Ground Glass",
	"Hypersensitivity Pneumonitis": "Allergies; Nodules-Illdefined",
	"Rb -ILD": "Smoking; Nodules-Illdefined",
	"DIP": "Smoking; Ground Glass-Diffuse",
	"Pulmonary Edema": "Ground Glass; Septal Thickening-Smooth; Perihilar; Fibrosis-Basal; Heart-Large",
	"COP": "Consolidation-Subpleural; Consolidation-Peripheral; Consolidation-Peribronchovascular; Reverse Halo",
	"Eosinophilic Pneumonia": "Eosinophilia; Consolidation-Subpleural; Consolidation-Peripheral; Consolidation-Peribronchovascular",
	"ABPA": "Halo Sign",
	"Opportunistic Infections": "Reverse Halo",
	"Old TB": "Fibrosis-Apical; Lymph Nodes-Calcifications",
	"TB": "Cavity-Smooth; Tree in Bud Lesion; Consolidation; Lymph Nodes; Pleural Effusion",
	"Sarcoidosis": "Lymph Nodes; Nodules-Peribronchovascular;",
	"Lymphangitis Carcinomatosa": "Septal Thickening-Irregular; Septal Thickening-Nodular; Septal Thickening-Unilateral",
	"PCP/CMV pneumonia": "Ground Glass-Diffuse; Immunocompromised",
	"Military TB": "Nodules-Random; Nodules-Bilateral"
}



# Create your views here.


# This view is used to capture the UID and store the clinic observations

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

		patientProfilePresent = clinicUserProfile.objects.filter(Q(uid=uniqueID))
		if patientProfilePresent:
			patientProfile = clinicUserProfile.objects.get(uid=uniqueID) 
			patientProfile.uid = uniqueID
			patientProfile.smokingHistory = smokingHistory
			patientProfile.allergies = allergies
			patientProfile.cough = cough
			patientProfile.fever = fever
			patientProfile.hemoptysis = hemoptysis
			patientProfile.breathlessness = breathlessness
			patientProfile.skinrash = skinrash
			patientProfile.tb = tb
			patientProfile.cvd = cvd
			patientProfile.sinusitis = sinusitis
			patientProfile.asthma = asthma
			patientProfile.dm = dm
			patientProfile.hiv = hiv
			patientProfile.save()
		else:
			userProfile = clinicUserProfile.objects.create(uid=uniqueID, smokingHistory=smokingHistory, allergies=allergies, cough=cough, fever=fever, hemoptysis=hemoptysis, breathlessness=breathlessness, skinrash=skinrash, tb=tb, cvd=cvd, sinusitis=sinusitis, asthma=asthma, dm=dm, hiv=hiv)
			userProfile.save()

		response = render(request, "thanks.html")
		return response

def viewChestClinicInfo(request, rid):
	
	if request.method == 'GET':
		patientProfilePresent = clinicUserProfile.objects.filter(Q(uid=str(rid)))
		if patientProfilePresent:
			request.session['radio-uid'] = str(rid)
			patientProfile = clinicUserProfile.objects.get(uid=request.session['radio-uid'])	
			patientDetails = {'smokingHistory': patientProfile.smokingHistory, 'allergies': patientProfile.allergies, 'cough': patientProfile.cough, 'fever': patientProfile.fever, 'hemoptysis':patientProfile.hemoptysis, 'breathlessness':patientProfile.breathlessness, 'skinrash':patientProfile.skinrash, 'tb':patientProfile.tb, 'cvd':patientProfile.cvd, 'sinusitis':patientProfile.sinusitis, 'asthma':patientProfile.asthma, 'dm':patientProfile.dm, 'hiv':patientProfile.hiv}
			return render(request, 'radio-chest.html',{'patientDetails': patientDetails})
		else:
			return render(request, 'radio-chest.html')

	if request.method == 'POST':
		symptomList = []

		#  Retrieving clinical observations
		patientProfile = clinicUserProfile.objects.get(uid=request.session['radio-uid'])
		if patientProfile.smokingHistory == 'Y':
			symptomList.append(str("Smoking"))
		#if patientProfile.smokingHistory != "NIL":
			#symptomList.append(str("Allergies"))

		# Radiologist findings
		honeycombing = request.POST.get('honeycombing', 'N')
		if honeycombing != 'N':
			symptomList.append(str("Honeycombing"))
		septal = request.POST.get('septal', "NULL")
		if septal != "NULL":
			symptomList.append(str(septal))
		groundGlass = request.POST.get('groundGlass', "NULL")
		if groundGlass != "NULL":
			symptomList.append(str(groundGlass))
		consolidation = request.POST.get('consolidation', "NULL")
		if consolidation != "NULL":
			symptomList.append(str(consolidation))
		fibrosis = request.POST.get('fibrosis', "NULL")
		if fibrosis != "NULL":
			symptomList.append(str(fibrosis))
		nodules = request.POST.get('nodules', "NULL")
		if nodules != "NULL":
			symptomList.append(str(nodules))
		massLesion = request.POST.get('massLesion', "N")
		if massLesion != "N":
			symptomList.append(str("Mass Lesion"))
		treeInBudLesion = request.POST.get('treeInBudLesion', "N")
		if treeInBudLesion != "N":
			symptomList.append(str("Tree in Bud Lesion"))
		airTrapping = request.POST.get('airTrapping', "N")
		if airTrapping != "N":
			symptomList.append(str("Air Trapping"))
		mosaicAttenuation = request.POST.get('mosaicAttenuation', "N")
		if mosaicAttenuation != "N":
			symptomList.append(str("Mosaic Attenuation"))
		bronchiectasis = request.POST.get('bronchiectasis', "NULL")
		if bronchiectasis != "NULL":
			symptomList.append(str(bronchiectasis))
		cavity = request.POST.get('cavity', "NULL")
		if cavity != "NULL":
			symptomList.append(str(cavity))
		cysts = request.POST.get('cysts', "NULL")
		if cysts != "NULL":
			symptomList.append(str(cysts))
		emphysema = request.POST.get('emphysema', "N")
		if emphysema != "N":
			symptomList.append(str("Emphysema"))
		lymphNodes = request.POST.get('lymphNodes', "NULL")
		if lymphNodes != "NULL":
			symptomList.append(str(lymphNodes))
		pleuralEffusion = request.POST.get('pleuralEffusion', "N")
		if pleuralEffusion != "N":
			symptomList.append(str("Pleural Effusion"))
		pleuralThickening = request.POST.get('pleuralThickening', "NULL")
		if pleuralThickening != "NULL":
			symptomList.append(str(pleuralThickening))
		crazyPaving = request.POST.get('crazyPaving', "N")
		if crazyPaving != "N":
			symptomList.append(str("Crazy Paving"))
		haloSign = request.POST.get('haloSign', "N")
		if haloSign != "N":
			symptomList.append(str("Halo Sign"))
		reverseHalo = request.POST.get('reverseHalo', "N")
		if reverseHalo != "N":
			symptomList.append(str("Reverse Halo"))
		fat = request.POST.get('fat', "N")
		if fat != "N":
			symptomList.append(str("Fat"))
		heart = request.POST.get('heart', "NULL")
		if heart != "NULL":
			symptomList.append(str(heart))
		uniqueID = request.session['radio-uid']

		""" Computing list of possible diagnosis """

		
		# Finding exact match for entered symptoms
		tempDict = diseaseDict.copy()
		for i in symptomList:
			for key in tempDict.keys():
				if i not in tempDict[key]:
					del tempDict[key]

		# Populating dictionary to display exact diagnosis on the template
		exactDiagnosis = []
		for key in tempDict:
			exactDiagnosis.append({str("disease"):str(key), str("symptoms"): str(diseaseDict[key])})
		

		# Populating list of diagnosis
		diagnosisList = []
		for i in symptomList:
			for key in diseaseDict:
				if i in diseaseDict[key]:
					diagnosisList.append(str(key))

		# Removing duplicates from the list
		tempList = set(diagnosisList)
		diagnosisList = list(tempList)

		# Populating result dict
		resultDict = []
		for i in diagnosisList:
			for key in diseaseDict:
				if i == key:
					resultDict.append({str("disease"):str(key), str("symptoms"): str(diseaseDict[key])})

		# Removing matches between resultDict and exactDiagnosis
		for i in exactDiagnosis:
			if i in resultDict:
				resultDict.remove(i)


		# Uncomment the bottom two lines to store radiologist findings in the DB
		#userProfile = radioUserProfileChest.objects.create(uid=uniqueID, honeycombing=honeycombing, septal=septal, groundGlass=groundGlass, consolidation=consolidation, fibrosis=fibrosis, nodules=nodules, massLesion=massLesion, treeInBudLesion=treeInBudLesion, airTrapping=airTrapping, mosaicAttenuation=mosaicAttenuation, bronchiectasis=bronchiectasis, cavity=cavity, cysts=cysts, emphysema=emphysema, lymphNodes=lymphNodes, pleuralEffusion=pleuralEffusion, pleuralThickening=pleuralThickening, crazyPaving=crazyPaving, haloSign=haloSign, reverseHalo=reverseHalo, fat=fat, heart=heart)
		#userProfile.save()

		# Creating dict for selected items
		selectedDict = []
		for i in symptomList:
			selectedDict.append({str("selectedItem"): str(i)})


		response = render(request, "diagnosis.html", {'possibleDiagnosis': resultDict, 'selectedSymptom': selectedDict, 'exactDiagnosis': exactDiagnosis})
		#response = render(request, "diagnosis.html", {'possibleDiagnosis': resultDict, 'selectedSymptom': selectedDict})
		return response













	