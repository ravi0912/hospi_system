from rtc.models import CRequest, Medicine, FollowUp, Complaint, Prescription, Registration, Doctor
from django.contrib.auth.models import User



def __getprescription(user,docpat):   ####docpat = 1 when user is a doctor else 0 when patient
	if(docpat == 1):
		prescription = Prescription.objects.order_by('prescription_time').filter( doctor__name = user )
	else:
		prescription  = Prescription.objects.order_by('prescription_time').filter(reg_no__reg_no = user) 
	return prescription 
	# if(docpat == 1):
	# 	prescription  = Prescription.objects.order_by('prescription_time').filter(doctor = user).values('doctor__name','medicine__name','reg_no__username','symptoms','prescription_time','disease','next_visit')
	# else:
	# 	prescription  = Prescription.objects.order_by('prescription_time').filter(reg_no__reg_no = user).values('doctor__name','medicine__name','reg_no__username','symptoms','prescription_time','disease','next_visit'	)
		

def getprescriptiondetails(user, docpat):
	prescriptions  = __getprescription(user,docpat)
	details = []
	j=0
	for i in prescriptions:
		cur = {}
		cur['doctor'] = i.doctor.name
		cur['reg_no'] = i.reg_no.reg_no
		cur['disease'] = i.disease
		cur['medicine'] = Prescription.objects.filter(prescription_time = i.prescription_time).values('medicine__name')
		cur['symptoms'] = i.symptoms
		cur['time'] = i.prescription_time
		cur['next_visit'] = i.next_visit
		details.append(cur)
	
	return details