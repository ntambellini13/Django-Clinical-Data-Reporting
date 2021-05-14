from django.shortcuts import render
from clinicalDataApp.models import Patient
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
