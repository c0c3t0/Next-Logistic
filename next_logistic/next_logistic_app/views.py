import requests
from django.shortcuts import render

from next_logistic.next_logistic_app.models import Employee


def get_employees(request):
    url = 'https://hub.dummyapis.com/employee?noofRecords=20&idStarts=1001'
    response = requests.get(url)
    data = response.json()

    for i in data:
        print(i)
        employee_data = Employee(
            firstName=i['firstName'],
            lastName=i['lastName'],
            email=i['email'],
            salary=i['salary'],
            age=i['age'],
            imageUrl=i['imageUrl'],
            contactNumber=i['contactNumber'],
        )
        employee_data.save()

    context = {
        'all_employees': Employee.objects.all()
    }

    return render(request, 'employees.html', context)
