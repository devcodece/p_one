from django.shortcuts import render
from . forms import NewDepartment
#FormView -
from django.views.generic import ListView
from django.views.generic.edit import FormView
from employee.models import Employee
from . models import Department
# Create your views here.

class DepartmentListView(ListView):
    template_name = 'department/list-departments.html'
    model = Department
    context_object_name = 'departments'

class NewDepartmentView(FormView):
    template_name = 'department/new-department.html'
    form_class = NewDepartment
    success_url = 'employee/list-all'

    def form_valid(self, form):
        #instancia del modelo Department
        depart = Department(
            name = form.cleaned_data['department'],
            short_name = form.cleaned_data['short_name']
        )
        depart.save()

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        Employee.objects.create(
            first_name = first_name,
            last_name = last_name,
            job = '1',
            department=depart,
        )
        return super(NewDepartmentView, self).form_valid(form)
