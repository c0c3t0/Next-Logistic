import requests
from django.shortcuts import render

from next_logistic.next_logistic_app.models import Employee


def get_employees(request):
    all_employees = {}
    url = 'https://hub.dummyapis.com/employee?noofRecords=100&idStarts=1001'
    response = requests.get(url)
    data = response.json()
    # print(data)

    for i in data:
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

        all_employees = Employee.objects.all()

    context = {
        'all_employees': all_employees
    }
        # print(all_employees)

    return render(request, 'employees.html', context)
