from django.contrib import admin
from .models import Doctor,Patient,Appointment

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'special')
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender','mobile', 'address')
admin.site.register(Patient, PatientAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'patient', 'date', 'time')
admin.site.register(Appointment, AppointmentAdmin)
