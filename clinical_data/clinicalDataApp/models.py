from django.db import models

class Patient(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class ClinicalData(models.Model):
    COMPONENT_NAMES=[('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')]
    component_name = models.CharField(choices=COMPONENT_NAMES, max_length=20)
    component_value = models.CharField(max_length=20)
    measured_date_time = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)   


