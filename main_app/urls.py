from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('login/', views.login_page, name='login_page'),
    path('role_selection/', views.role_selection, name='role_selection'),
    path('patient_registration/', views.patient_registration, name='patient_registration'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('results/', views.results, name='results'),
    path('doctor_interface/', views.doctor_interface, name='doctor_interface'),
    path('pharmacy_interface/', views.pharmacy_interface, name='pharmacy_interface'),
    path('welcome_page/', views.welcome_page, name='welcome_page')
]
