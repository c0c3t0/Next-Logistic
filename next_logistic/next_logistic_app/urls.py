from django.urls import path

from next_logistic.next_logistic_app import views

urlpatterns = [
    path('', views.get_employees, name='get employees')
]
