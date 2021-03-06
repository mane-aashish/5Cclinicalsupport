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

# changed entry = "Pulmonary Edema": "Ground Glass-Focal; Ground Glass-Diffuse; Ground Glass-Patchy; Septal Thickening-Smooth; Heart-Large"

diseaseDict = {
	"UIP": "Honeycombing; Fibrosis-Basal; Fibrosis-Subpleural; Collagen Vascular Disease; Skin Rash/Arthritis/Joint Pain",
	"NSIP": "Septal Thickening-Irregular; Fibrosis-Mixed; Ground Glass-Focal; Ground Glass-Diffuse; Ground Glass-Patchy; Collagen Vascular Disease; Skin Rash/Arthritis/Joint Pain",
	"Hypersensitivity Pneumonitis": "Allergies; Nodules-Centrilobular; Air Trapping",
	"Rb -ILD": "Smoking; Nodules-Centrilobular; Tree in Bud Lesion",
	"DIP": "Smoking; Ground Glass-Focal; Ground Glass-Diffuse; Ground Glass-Patchy",
	"Pulmonary Edema": "Crazy Paving; Heart-Large",
	"COP": "Consolidation-Subpleural; Consolidation-Peripheral; Consolidation-Peribronchovascular; Reverse Halo",
	"Eosinophilic Pneumonia": "Eosinophilia; Consolidation-Subpleural; Consolidation-Peripheral; Consolidation-Peribronchovascular",
	"Invasive Aspergillosis": "Halo Sign",
	"Opportunistic Infections": "Reverse Halo",
	"Old TB": "Fibrosis-Apical; Lymph Nodes-Calcifications",
	"TB": "Cavity-Smooth; Tree in Bud Lesion; Consolidation; Pleural Effusion; Lymph Nodes-Unilateral; Lymph Nodes-Bilateral; Lymph Nodes-Hilar; Lymph Nodes-Calcifications",
	"Sarcoidosis": "Lymph Nodes-Calcifications; Lymph Nodes-Hilar; Nodules-Peribronchovascular; Nodules-Fissural",
	"Lymphangitis Carcinomatosa": "Septal Thickening-Irregular; Septal Thickening-Nodular; Septal Thickening-Unilateral",
	"PCP/CMV pneumonia": "Ground Glass-Diffuse; HIV/Immunocompromised",
	"Military TB": "Nodules-Random; Nodules-Bilateral",
	"ARDS": "Consolidation-Bilateral; Consolidation-Acute; Ground Glass-Focal; Ground Glass-Diffuse; Ground Glass-Patchy",
	"Lymphoid Interstitial Pneumonia": "HIV/Immunocompromised; Cysts-Thin Wall",
	"Langerhans Cell Histiocytosis": "Smoking; Cysts-Thick Wall; Cysts-Irregular",
	"Chronic Hypersensitivity": "Fibrosis-Mid",
	"Constrictive Bronchiolitis/ Chronic Pulmonary Thromboembolism": "Mosaic Attenuation",
	"Hypersensitivity Pneumonitis": "Mosaic Attenuation; Allergies",
	"Lipoid Pneumonia": "Consolidation; Fat",
	"Silicosis": "Mining/Tunnel Work; Nodules-Bilateral; Lymph Nodes-Calcifications",
	"Combined Pulmonary Fibrosis and Emphysema": "Emphysema; Septal Thickening-Irregular",
	"Alveolar proteinosis/ARDS/AIP; COP/PCP,Hemorrhage/BAC": "Septal Thickening-Irregular; Crazy Paving"
}



# Create your views here.


# This view is used to capture the UID and store the clinic observations

def storeClinicInfo(request, rid):

	if request.method == 'GET':
		request.session['uid'] = str(rid)
		return render(request, "clinic.html")

	
	if request.method == 'POST':
		sex = request.POST.get('sex', "MALE")
		#sex = request.POST.getlist('sex')
		age = request.POST.get('age', "25")
		smokingHistory = request.POST.get('smoking', 'N')
		allergies = request.POST.get('allergies', "NIL")
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
		eosinophilia = request.POST.get('eosinophilia', 'N')
		hiv = request.POST.get('hiv', 'N')
		mining = request.POST.get('mining', 'N')
		uniqueID = request.session['uid']

		patientProfilePresent = clinicUserProfile.objects.filter(Q(uid=uniqueID))
		if patientProfilePresent:
			patientProfile = clinicUserProfile.objects.get(uid=uniqueID) 
			patientProfile.uid = uniqueID
			patientProfile.sex = sex
			patientProfile.age = age
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
			patientProfile.eosinophilia = eosinophilia
			patientProfile.hiv = hiv
			patientProfile.mining = mining
			patientProfile.save()
		else:
			userProfile = clinicUserProfile.objects.create(uid=uniqueID, sex=sex, age=age, smokingHistory=smokingHistory, allergies=allergies, cough=cough, fever=fever, hemoptysis=hemoptysis, breathlessness=breathlessness, skinrash=skinrash, tb=tb, cvd=cvd, sinusitis=sinusitis, asthma=asthma, dm=dm, hiv=hiv, mining=mining, eosinophilia=eosinophilia)
			userProfile.save()

		response = render(request, "thanks.html")
		return response



def viewChestClinicInfo(request, rid):
	
	if request.method == 'GET':
		patientProfilePresent = clinicUserProfile.objects.filter(Q(uid=str(rid)))
		if patientProfilePresent:
			request.session['radio-uid'] = str(rid)
			patientProfile = clinicUserProfile.objects.get(uid=request.session['radio-uid'])	
			patientDetails = {'sex': patientProfile.sex, 'age' : patientProfile.age , 'smokingHistory': patientProfile.smokingHistory, 'allergies': patientProfile.allergies, 'cough': patientProfile.cough, 'fever': patientProfile.fever, 'hemoptysis':patientProfile.hemoptysis, 'breathlessness':patientProfile.breathlessness, 'skinrash':patientProfile.skinrash, 'tb':patientProfile.tb, 'cvd':patientProfile.cvd, 'sinusitis':patientProfile.sinusitis, 'asthma':patientProfile.asthma, 'dm':patientProfile.dm, 'hiv':patientProfile.hiv, 'mining':patientProfile.mining, 'eosinophilia':patientProfile.eosinophilia}
			return render(request, 'radio-chest.html',{'patientDetails': patientDetails})
		else:
			return render(request, 'radio-chest.html')

	if request.method == 'POST':
		symptomList = []
		symptomList2 = []

		#  Retrieving clinical observations
		patientProfile = clinicUserProfile.objects.get(uid=request.session['radio-uid'])
		if patientProfile.smokingHistory == 'Y':
			symptomList.append(str("Smoking"))
			symptomList2.append(str("Smoking"))
		if patientProfile.allergies != "NIL":
			symptomList.append(str("Allergies"))
			symptomList2.append(str("Allergies"))
		if patientProfile.hiv == 'Y':
			symptomList.append(str("HIV/Immunocompromised"))
			symptomList2.append(str("HIV/Immunocompromised"))
		if patientProfile.eosinophilia == 'Y':
			symptomList.append(str("Eosinophilia"))
			symptomList2.append(str("Eosinophilia"))
		if patientProfile.mining == 'Y':
			symptomList.append(str("Mining/Tunnel Work"))
			symptomList2.append(str("Mining/Tunnel Work"))
		if patientProfile.cvd == 'Y':
			symptomList.append(str("Collagen Vascular Disease"))
			symptomList2.append(str("Collagen Vascular Disease"))
		if patientProfile.skinrash == 'Y':
			symptomList.append(str("Skin Rash/Arthritis/Joint Pain"))
			symptomList2.append(str("Skin Rash/Arthritis/Joint Pain"))

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
		#consolidation = request.POST.get('consolidation', "NULL")
		consolidation = request.POST.getlist('consolidation')
		consolidationDB = ";".join(consolidation)
		if len(consolidation) != 0:
			for i in consolidation:
				symptomList.append(str(i))
		else:
			consolidationDB="NULL"
		#Consolidation-Iobar
		print symptomList
		fibrosis = request.POST.get('fibrosis', "NULL")
		if fibrosis != "NULL":
			symptomList.append(str(fibrosis))
		#nodules = request.POST.get('nodules', "NULL")
		nodules = request.POST.getlist('nodules')
		nodulesDB = ";".join(nodules)
		if len(nodules) != 0:
			for i in nodules:
				symptomList.append(str(i))
		else:
			nodulesDB="NULL"
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

		# Computing list of possible diagnosis

		
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
		for i in symptomList2:
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


		# Creating dict for selected items
		selectedDict = []
		for i in symptomList:
			selectedDict.append({str("selectedItem"): str(i)})

		# Special case for LAM
		if str("Cysts-Thin Wall") in symptomList and patientProfile.sex == "FEMALE" and int(patientProfile.age) < 40:
			exactDiagnosis.append({str("disease"):str("LAM"), str("symptoms"): str("Cysts-Thin Wall; Premenopausal Female")}) 
		

		# Storing information in the DB
		profilePresent = radioUserProfileChest.objects.filter(Q(uid=uniqueID))
		if profilePresent:
			profile = radioUserProfileChest.objects.get(uid=uniqueID)
			profile.uid = uniqueID
			profile.honeycombing=honeycombing
			profile.septal=septal
			profile.groundGlass=groundGlass
			profile.consolidation=consolidationDB
			profile.fibrosis=fibrosis
			profile.nodules=nodulesDB
			profile.massLesion=massLesion
			profile.treeInBudLesion=treeInBudLesion
			profile.airTrapping=airTrapping
			profile.mosaicAttenuation=mosaicAttenuation
			profile.bronchiectasis=bronchiectasis
			profile.cysts=cysts
			profile.cavity=cavity
			profile.emphysema=emphysema
			profile.lymphNodes=lymphNodes
			profile.pleuralEffusion=pleuralEffusion
			profile.pleuralThickening = pleuralThickening
			profile.crazyPaving=crazyPaving
			profile.haloSign=haloSign
			profile.reverseHalo=reverseHalo
			profile.fat=fat
			profile.heart=heart
			profile.save()
		else:
			userProfile = radioUserProfileChest.objects.create(uid=uniqueID, honeycombing=honeycombing, septal=septal, groundGlass=groundGlass, consolidation=consolidationDB, fibrosis=fibrosis, nodules=nodulesDB, massLesion=massLesion, treeInBudLesion=treeInBudLesion, airTrapping=airTrapping, mosaicAttenuation=mosaicAttenuation, bronchiectasis=bronchiectasis, cavity=cavity, cysts=cysts, emphysema=emphysema, lymphNodes=lymphNodes, pleuralEffusion=pleuralEffusion, pleuralThickening=pleuralThickening, crazyPaving=crazyPaving, haloSign=haloSign, reverseHalo=reverseHalo, fat=fat, heart=heart)
			userProfile.save()
		
		

		response = render(request, "diagnosis.html", {'possibleDiagnosis': resultDict, 'selectedSymptom': selectedDict, 'exactDiagnosis': exactDiagnosis})
		#response = render(request, "diagnosis.html", {'possibleDiagnosis': resultDict, 'selectedSymptom': selectedDict})
		return response


def viewChestDiagnosis(request, rid):
	uniqueID = str(rid)
	# Initializing symptom list
	symptomList = []
	symptomList2 = []

	# Checking if required information has been recorded
	profileClinicPresent = radioUserProfileChest.objects.filter(Q(uid=uniqueID))
	profileRadioPresent = radioUserProfileChest.objects.filter(Q(uid=uniqueID))

	if profileClinicPresent and profileRadioPresent:
		#  Retrieving clinical observations
		patientClinicProfile = clinicUserProfile.objects.get(uid=uniqueID)
		if patientClinicProfile.smokingHistory == 'Y':
			symptomList.append(str("Smoking"))
			symptomList2.append(str("Smoking"))
		if patientClinicProfile.allergies != "NIL":
			symptomList.append(str("Allergies"))
			symptomList2.append(str("Allergies"))
		if patientClinicProfile.hiv == 'Y':
			symptomList.append(str("HIV/Immunocompromised"))
			symptomList2.append(str("HIV/Immunocompromised"))
		if patientClinicProfile.eosinophilia == 'Y':
			symptomList.append(str("Eosinophilia"))
			symptomList2.append(str("Eosinophilia"))
		if patientClinicProfile.mining == 'Y':
			symptomList.append(str("Mining/Tunnel Work"))
			symptomList2.append(str("Mining/Tunnel Work"))
		if patientClinicProfile.cvd == 'Y':
			symptomList.append(str("Collagen Vascular Disease"))
			symptomList2.append(str("Collagen Vascular Disease"))
		if patientClinicProfile.skinrash == 'Y':
			symptomList.append(str("Skin Rash/Arthritis/Joint Pain"))
			symptomList2.append(str("Skin Rash/Arthritis/Joint Pain"))

		# Retrieving radiologist information
		patientRadioProfile = radioUserProfileChest.objects.get(uid=uniqueID)
		if patientRadioProfile.honeycombing != 'N':
			symptomList.append(str("Honeycombing"))
		if patientRadioProfile.septal != "NULL":
			symptomList.append(str(patientRadioProfile.septal))
		if patientRadioProfile.groundGlass != "NULL":
			symptomList.append(str(patientRadioProfile.groundGlass))
		if patientRadioProfile.consolidation != "NULL":
			x = patientRadioProfile.consolidation.split(';')
			for i in x:
				symptomList.append(str(i))
		if patientRadioProfile.fibrosis != "NULL":
			symptomList.append(str(patientRadioProfile.fibrosis))
		if patientRadioProfile.nodules != "NULL":
			y = patientRadioProfile.nodules.split(';')
			for i in y:
				symptomList.append(str(i))
		if patientRadioProfile.massLesion != "N":
			symptomList.append(str("Mass Lesion"))
		if patientRadioProfile.treeInBudLesion != "N":
			symptomList.append(str("Tree in Bud Lesion"))
		if patientRadioProfile.airTrapping != "N":
			symptomList.append(str("Air Trapping"))
		if patientRadioProfile.mosaicAttenuation != "N":
			symptomList.append(str("Mosaic Attenuation"))
		if patientRadioProfile.bronchiectasis != "NULL":
			symptomList.append(str(patientRadioProfile.bronchiectasis))
		if patientRadioProfile.cavity != "NULL":
			symptomList.append(str(patientRadioProfile.cavity))
		if patientRadioProfile.cysts != "NULL":
			symptomList.append(str(patientRadioProfile.cysts))
		if patientRadioProfile.emphysema != "N":
			symptomList.append(str("Emphysema"))
		if patientRadioProfile.lymphNodes != "NULL":
			symptomList.append(str(patientRadioProfile.lymphNodes))
		if patientRadioProfile.pleuralEffusion != "N":
			symptomList.append(str("Pleural Effusion"))
		if patientRadioProfile.pleuralThickening != "NULL":
			symptomList.append(str(patientRadioProfile.pleuralThickening))
		if patientRadioProfile.crazyPaving != "N":
			symptomList.append(str("Crazy Paving"))
		if patientRadioProfile.haloSign != "N":
			symptomList.append(str("Halo Sign"))
		if patientRadioProfile.reverseHalo != "N":
			symptomList.append(str("Reverse Halo"))
		if patientRadioProfile.fat != "N":
			symptomList.append(str("Fat"))
		if patientRadioProfile.heart != "NULL":
			symptomList.append(str(patientRadioProfile.heart))

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
		for i in symptomList2:
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


		# Creating dict for selected items
		selectedDict = []
		for i in symptomList:
			selectedDict.append({str("selectedItem"): str(i)})

		# Special case for LAM
		if str("Cysts-Thin Wall") in symptomList and patientClinicProfile.sex == "FEMALE" and int(patientClinicProfile.age) < 40:
			exactDiagnosis.append({str("disease"):str("LAM"), str("symptoms"): str("Cysts-Thin Wall; Premenopausal Female")}) 


		response = render(request, "viewdiagnosis.html", {'possibleDiagnosis': resultDict, 'selectedSymptom': selectedDict, 'exactDiagnosis': exactDiagnosis})	
		return response
	else:
		response = render(request, "nodiagnosis.html")
		return response	
	













	