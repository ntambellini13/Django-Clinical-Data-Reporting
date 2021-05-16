"""clinical_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clinicalDataApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PatientListView.as_view(), name='index'),
    path('create/', views.PatientCreateView.as_view(), name='add_patient'),
    path('update/<int:pk>/', views.PatientUpdateView.as_view(), name='update_patient'),
    path('delete/<int:pk>/', views.PatientDeleteView.as_view(), name='delete_patient'),
    path('add-data/<int:pk>/', views.add_data, name='add_patient_data'),
    path('analyze-bmi/<int:pk>/', views.analyze_bmi, name='analyze_patient_bmi'),
]
