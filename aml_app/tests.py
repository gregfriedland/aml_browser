import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Patient


class PatientModelTests(TestCase):

    def test_create_empty(self):
    	p = Patient()
    	