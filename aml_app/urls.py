from django.urls import path

from . import views

urlpatterns = [
    # ex: /aml
    path('', views.index, name='index'),
    # ex: /aml/5/
    path('<int:patient_pk>/', views.detail, name='detail'),
]
