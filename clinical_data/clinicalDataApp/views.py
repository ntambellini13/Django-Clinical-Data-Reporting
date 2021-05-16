from django.shortcuts import render, redirect
from clinicalDataApp.models import Patient, ClinicalData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clinicalDataApp.forms import ClinicalDataForm

class PatientListView(ListView):
    model=Patient

class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('first_name', 'last_name', 'age')

class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('first_name', 'last_name', 'age')

class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')

def add_data(request, **kwargs):
    form = ClinicalDataForm
    patient = Patient.objects.get(id=kwargs['pk'])
    
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalDataApp/clinical_data_form.html', {'form':form, 'patient':patient})

def analyze_bmi(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    response_data = []
    for value in data:
        if value.component_name == 'hw':
            
            height_and_weight = value.component_value.split('/')
            if len(height_and_weight) > 1:
                feet_to_metres = float(height_and_weight[0]) * 0.4536
                bmi = (float(height_and_weight[1])/(feet_to_metres*feet_to_metres))
                bmi_value = ClinicalData()
                bmi_value.component_name = 'bmi'
                bmi_value.component_value = bmi
                response_data.append(bmi_value)
        response_data.append(value)
    return render(request, 'clinicalDataApp/generate_patient_report.html', {'data':response_data})