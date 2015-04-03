from django.contrib import admin
from rtc.models import CRequest,Medicine,FollowUp , Complaint
# Register your models here.
admin.site.register(CRequest)
admin.site.register(Medicine)
admin.site.register(FollowUp)
admin.site.register(Complaint)