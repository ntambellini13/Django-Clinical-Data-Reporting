from django.shortcuts import render, redirect
from clinicalDataApp.models import Patient
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