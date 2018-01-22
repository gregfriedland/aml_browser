from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Patient

def detail(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    return render(request, 'aml_app/detail.html', {'patient': patient})

def index(request):
    patients = Patient.objects.order_by('patient_id')
    return render(request, 'aml_app/index.html', {'patients': patients})
