from django.shortcuts import render ,redirect
from django.http import HttpResponse
import requests

from django.conf import settings
import requests as req
import json

MAIN_URL = "https://rooftop-uat.mpcz.in:8443/acr/"

from django.http import HttpResponse
from django.views.generic import View
from xhtml2pdf import pisa
 
#importing get_template from loader
from django.template.loader import get_template
 
#import render_to_pdf from util.py 
from .utils import render_to_pdf 
 
#Creating our view, it is a class based view
# class GeneratePdf(View):
#      def get(self, request, *args, **kwargs):
        
#         #getting the template
#         pdf = render_to_pdf('lll.html')
         
#          #rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')



def BirthCertificate_PDF(request,id) :
	URL= f"{MAIN_URL}/acrbyacrid/{id}"
	api = requests.get(URL,verify=False).json()
	data = api["object"]
	val_01 = api["object"]["firstApoointmentDesignation"]
	val_02 = api["object"]["presentApoointmentDesignation"]
	## second api 
	URL_1 = f"{MAIN_URL}/employee/{data.get('empId')}"
	api_1 = requests.get(URL_1,verify=False).json()
	data_1 = api_1["object"]
	# third api 
	URL_2 = f"{MAIN_URL}/getjobassignment/{id}"
	api_2 = requests.get(URL_2,verify=False).json()
	data_2 = api_2["object"]
	URL_3 = f"{MAIN_URL}/kpianswer/{id}"
	api_3 = requests.get(URL_3,verify=False).json()
	data_3 = api_3["object"]
	val = api_3["object"][1]["isfieldKpi"]
	val_001 = api_3["object"][0]["kpiId"]

	URL_33 = f"{MAIN_URL}/kpibyid/{val_001}"
	api_33 = requests.get(URL_33,verify=False).json()
	data_33 = api_33["object"]



	URL_4 = f"{MAIN_URL}/kpimtr/{id}"
	api_4 = requests.get(URL_4,verify=False).json()
	data_4 = api_4["object"]

	URL_5 = f"{MAIN_URL}/fixedkpi/{id}"
	api_5 = requests.get(URL_5,verify=False).json()
	data_5 = api_5["object"]

	URL_6 = f"{MAIN_URL}/freekpi/{id}"
	api_6 = requests.get(URL_6,verify=False).json()
	data_6 = api_6["object"]
	
	URL_7 = f"{MAIN_URL}/utility/designationbyid/{val_01}"
	api_7 = requests.get(URL_7,verify=False).json()
	data_7 = api_7["object"]

	URL_8 = f"{MAIN_URL}/utility/designationbyid/{val_02}"
	api_8 = requests.get(URL_8,verify=False).json()
	data_8 = api_8["object"]

	all_data = f"{MAIN_URL}/reportingformbyacrid/{id}"
	all_data_value = requests.get(all_data,verify=False).json()
	all_get = all_data_value["object"]
	one = all_get[0]["listOfAcrReportingQue"]
	two = all_get[0]["listOfAcrReportingPersonalAttribute"]
	three = all_get[0]["listOfAcrReportingKpiAnswer"]
	four = all_get[0]["listOfAcrReportingOtherKpiAnswer"]
	data = {'four':four,'three':three,'two':two,'one':one,'all_get':all_get,'id':id,'data':data
	,'data_1':data_1,'data_2':data_2,'data_3':data_3,'data_33':data_33,'data_4':data_4,'data_5':data_5,'data_6':data_6,'data_7':data_7,'data_8':data_8,'val':val}
	template = get_template('lll.html')
	html  = template.render(data)
	file = open('lll.pdf', "w+b")
	pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
		encoding='utf-8')
	file.seek(0)
	pdf = file.read()
	file.close()
	return HttpResponse(pdf, 'application/pdf')


def acr_data(request,id):
	URL = f"{MAIN_URL}/kpimtr/{id}"
	URL_1 = f"{MAIN_URL}/freekpi/{id}"

	api_data = requests.get(URL,verify=False).json()
	api_data1 = requests.get(URL_1,verify=False).json()

	data0 = api_data["object"]
	data_1 = api_data1["object"]
	URL_2 = f"{MAIN_URL}/kpianswer/{id}"
	api_data2 = requests.get(URL_2,verify=False).json()
	

	data_2 = api_data2["object"]
	URL_3 = f"{MAIN_URL}/kpianswer/{id}"
	api_3 = requests.get(URL_3,verify=False).json()
	data_3 = api_3["object"]
	val = api_3["object"][1]["isfieldKpi"]
	if request.method == "POST":
		kpi_list = request.POST.getlist('kpi')

		startOfFy_list = request.POST.getlist('startOfFy')
		endOfFy_list = request.POST.getlist('endOfFy')
		grade_list = request.POST.getlist('grade')
		
		Reportingkpi = request.POST.getlist('Reportingkpi')
		ReportingstartOfFy = request.POST.getlist('ReportingstartOfFy')
		ReportingendOfFy = request.POST.getlist('ReportingendOfFy')
		Reportingachievements = request.POST.getlist('Reportingachievements')
		Reportingremark = request.POST.getlist('Reportingremark')
		Reportinggrade = request.POST.getlist('Reportinggrade')

		personalAttributes = request.POST.getlist('personalAttributes')
		personalgrade = request.POST.getlist('personalgrade')

		commentOne = request.POST.get('commentOne')
		commentTwo = request.POST.get('commentTwo')
		commentThree = request.POST.get('commentThree')
		commentFour = request.POST.get('commentFour')
		isAppraiseeRelative = request.POST.get('isAppraiseeRelative')
		adverseRemark = request.POST.get('adverseRemark')
		inCaseOf = request.POST.get('inCaseOf')
		generalAssessment = request.POST.get('generalAssessment')
		reviewOfPerformance = request.POST.get('reviewOfPerformance')
		identification = request.POST.get('identification')
		properAssignmentsOfTasks = request.POST.get('properAssignmentsOfTasks')
		persuasiveness = request.POST.get('persuasiveness')
		clearGuidance = request.POST.get('clearGuidance')
		organizingCapacity = request.POST.get('organizingCapacity')
		ripeUnderstanding = request.POST.get('ripeUnderstanding')
		commitment = request.POST.get('commitment')
		abilityToContribute = request.POST.get('abilityToContribute')
		abilityToWithstands = request.POST.get('abilityToWithstands')
		URL =  "https://rooftop-uat.mpcz.in:8443/acr/submitroform"
		data={
		"abilityToContribute": abilityToContribute,
		"abilityToWithstands": abilityToWithstands,
		"acrId": id,
		"acrReportingKpiAnswers":
		[{
		"achievements": "string",
		"createdTime": "string",
		"endOfFy": c,
		"grade": d,
		"kpi": a,
		"remark": "string",
		"startOfFy":b
		}for a,b,c,d in zip(kpi_list,startOfFy_list,endOfFy_list,grade_list)],
		  "acrReportingOtherKpiAnswers": [ 
		    {
		      "achievements": c,

		      "createdTime": "string",
		      "endOfFy": c,
		      "grade": f,
		      "kpi": a,
		      "remark": e,
		      "startOfFy": b
		    }for a,b,c,d,e,f in zip(Reportingkpi,ReportingstartOfFy,ReportingendOfFy,Reportingachievements,Reportingremark,
		    	Reportinggrade)
		  ],
		  "acrReportingPersonalAttributes": [
		    {

		      "grade": a,
		      "personalAttributes": b
		    }for a,b in zip(personalgrade,personalAttributes)
		  ],
		  "adverseRemark": adverseRemark,
		  "clearGuidance": clearGuidance,
		  "commentFour": commentFour,
		  "commentOne": commentOne,
		  "commentThree": commentThree,
		  "commentTwo": commentTwo,
		  "commitment": commitment,
		  "createdDate": "string",
		  "finalGrading": "string",
		  "generalAssessment": generalAssessment,
		  "grade": "string",
		  "identification": identification,
		  "inCaseOf": inCaseOf,
		  "isAppraiseeRelative": isAppraiseeRelative,
		  "organizingCapacity": organizingCapacity,
		  "persuasiveness": persuasiveness,
		  "points": "string",
		  "properAssignmentsOfTasks": properAssignmentsOfTasks,
		  "remarksToBeConveyed": "string",
		  "reportingOffEmpCode": 1234,
		  "reviewOfPerformance": reviewOfPerformance,
		  "ripeUnderstanding": ripeUnderstanding,
		  "weightageOne": "string",
		  "weightageThree": "string",
		  "weightageTwo": "string"
		}
		json_data = json.dumps(data)
		# print('-----------------------',json_data)
		print('jjjjjjjjjjjj',json_data)
		headers = {'Content-type': 'application/json'}
		res = req.request('POST',url=URL,data=json_data,headers=headers,verify=False)
		print(res)
		return redirect(f'/pdf/{id}')

	return render(request,'home.html',{'data':data0,'data_1':data_1,'data_2':data_2,'id':id,'val':val})

def Appraisee(request):
	URL="https://rooftop-uat.mpcz.in:8443/acr/getacrbyreportingcode/11330098"
	data = requests.get(URL,verify=False).json()
	a1 = data["object"]
	
	return render(request,'Appraisee_list.html',{'data':a1})



def Personal_Data(request,id):
	URL= f"{MAIN_URL}/acrbyacrid/{id}"
	api = requests.get(URL,verify=False).json()
	data = api["object"]
	val_01 = api["object"]["firstApoointmentDesignation"]
	val_02 = api["object"]["presentApoointmentDesignation"]
	## second api 
	URL_1 = f"{MAIN_URL}/employee/{data.get('empId')}"
	api_1 = requests.get(URL_1,verify=False).json()
	data_1 = api_1["object"]
	# third api 
	URL_2 = f"{MAIN_URL}/getjobassignment/{id}"
	api_2 = requests.get(URL_2,verify=False).json()
	data_2 = api_2["object"]
	URL_3 = f"{MAIN_URL}/kpianswer/{id}"
	api_3 = requests.get(URL_3,verify=False).json()
	data_3 = api_3["object"]
	val = api_3["object"][1]["isfieldKpi"]
	val_001 = api_3["object"][0]["kpiId"]

	URL_33 = f"{MAIN_URL}/kpibyid/{val_001}"
	api_33 = requests.get(URL_33,verify=False).json()
	data_33 = api_33["object"]



	URL_4 = f"{MAIN_URL}/kpimtr/{id}"
	api_4 = requests.get(URL_4,verify=False).json()
	data_4 = api_4["object"]

	URL_5 = f"{MAIN_URL}/fixedkpi/{id}"
	api_5 = requests.get(URL_5,verify=False).json()
	data_5 = api_5["object"]

	URL_6 = f"{MAIN_URL}/freekpi/{id}"
	api_6 = requests.get(URL_6,verify=False).json()
	data_6 = api_6["object"]
	
	URL_7 = f"{MAIN_URL}/utility/designationbyid/{val_01}"
	api_7 = requests.get(URL_7,verify=False).json()
	data_7 = api_7["object"]

	URL_8 = f"{MAIN_URL}/utility/designationbyid/{val_02}"
	api_8 = requests.get(URL_8,verify=False).json()
	data_8 = api_8["object"]



	return render(request,'Personal_Data.html',{'id':id,'data':data,'data_1':data_1,
		'data_2':data_2,'data_3':data_3,'data_33':data_33,'data_4':data_4,'data_5':data_5,'data_6':data_6,'data_7':data_7,'data_8':data_8,'val':val})
# Create your views here.


def pdf(request,id):
	URL= f"{MAIN_URL}/acrbyacrid/{id}"
	api = requests.get(URL,verify=False).json()
	data = api["object"]
	val_01 = api["object"]["firstApoointmentDesignation"]
	val_02 = api["object"]["presentApoointmentDesignation"]
	## second api 
	URL_1 = f"{MAIN_URL}/employee/{data.get('empId')}"
	api_1 = requests.get(URL_1,verify=False).json()
	data_1 = api_1["object"]
	# third api 
	URL_2 = f"{MAIN_URL}/getjobassignment/{id}"
	api_2 = requests.get(URL_2,verify=False).json()
	data_2 = api_2["object"]
	URL_3 = f"{MAIN_URL}/kpianswer/{id}"
	api_3 = requests.get(URL_3,verify=False).json()
	data_3 = api_3["object"]
	val = api_3["object"][1]["isfieldKpi"]
	val_001 = api_3["object"][0]["kpiId"]

	URL_33 = f"{MAIN_URL}/kpibyid/{val_001}"
	api_33 = requests.get(URL_33,verify=False).json()
	data_33 = api_33["object"]



	URL_4 = f"{MAIN_URL}/kpimtr/{id}"
	api_4 = requests.get(URL_4,verify=False).json()
	data_4 = api_4["object"]

	URL_5 = f"{MAIN_URL}/fixedkpi/{id}"
	api_5 = requests.get(URL_5,verify=False).json()
	data_5 = api_5["object"]

	URL_6 = f"{MAIN_URL}/freekpi/{id}"
	api_6 = requests.get(URL_6,verify=False).json()
	data_6 = api_6["object"]
	
	URL_7 = f"{MAIN_URL}/utility/designationbyid/{val_01}"
	api_7 = requests.get(URL_7,verify=False).json()
	data_7 = api_7["object"]

	URL_8 = f"{MAIN_URL}/utility/designationbyid/{val_02}"
	api_8 = requests.get(URL_8,verify=False).json()
	data_8 = api_8["object"]

	all_data = f"{MAIN_URL}/reportingformbyacrid/{id}"
	all_data_value = requests.get(all_data,verify=False).json()
	all_get = all_data_value["object"]
	one = all_get[0]["listOfAcrReportingQue"]
	two = all_get[0]["listOfAcrReportingPersonalAttribute"]
	three = all_get[0]["listOfAcrReportingKpiAnswer"]
	four = all_get[0]["listOfAcrReportingOtherKpiAnswer"]


	return render(request,'pdf.html',{'four':four,'three':three,'two':two,'one':one,'all_get':all_get,'id':id,'data':data,'data_1':data_1,
		'data_2':data_2,'data_3':data_3,'data_33':data_33,'data_4':data_4,'data_5':data_5,'data_6':data_6,'data_7':data_7,'data_8':data_8,'val':val})