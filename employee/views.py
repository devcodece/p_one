from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from . models import Employee
from  django.urls import reverse_lazy
from django.db.models import Q
from . forms import EmployeeForm

# Create your views here.

class HomeView(TemplateView):
    """ Vista que carga la pagina de inicio """
    template_name = 'home.html'


class ListAllEmployees(ListView):
    template_name = 'employee/list-all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'employees'

    def get_queryset(self):
        word_key = self.request.GET.get('kword', '')
        
        list = Employee.objects.filter(
            Q(first_name__icontains = word_key) | Q(last_name__icontains = word_key)
        )
        return list

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/detail-employee.html'

    def get_context_data(self, **kwargs):
        context =  super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Empleado del mes'
        return context

class ListByArea(ListView):
    template_name = 'employee/list-by-area.html'
    context_object_name = 'employees_area'
    #Sobre-escribiendo el metodo get_queryset(self)
    def get_queryset(self):
        #recogiendo la variable shortname de la url
        area = self.kwargs['shortname']
        list = Employee.objects.filter(
            department__short_name = area
        )
        return list

class ListAllEmployeesAdmin(ListView):
    template_name = 'employee/list-all-admin.html'
    paginate_by = 8
    ordering = 'id'
    context_object_name = 'employees'
    model = Employee


class ListBySearch(ListView):
    template_name = 'list-by-search.html'
    context_object_name = 'employees'

    def get_queryset(self):

        word_key = self.request.GET.get('kword', '')

        list = Employee.objects.filter(
            first_name = word_key
        )
        return list

class ListSkills(ListView):
    template_name = 'list-skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        e = Employee.objects.get(id = 5)
        return e.skill.all()


#Esta vista solo funciona con un template
class SuccessView(TemplateView):
    template_name = 'employee/success.html'

class EmployeeCreateView(CreateView):
    template_name = 'employee/add-employee.html'
    model = Employee
    #Utilizando form.py
    form_class = EmployeeForm

    #Es necesario un paramentro que haga referencia a los campos del model
    """ fields  = [
        'first_name',
        'last_name',
        'job',
        'department',
        'skill',
        'avatar',
    ] """

    #fields = ('__all__')
    #Recargar la misma pagina
    success_url = reverse_lazy('list-all')

    #Se intercepta los datos que se guardan y se guardar los datos del nuevo campo full_name
    def form_valid(self, form):
        #Para que no se guarde el registro se agrega commir=False
        employee = form.save(commit=False)
        employee.full_name = employee.first_name + ' ' + employee.last_name
        employee.save()
        return super(EmployeeCreateView, self).form_valid(form)


class EmployeeUpdateView(UpdateView):
    template_name = 'employee/update.html'
    model = Employee
    fields  = [
        'first_name',
        'last_name',
        'job',
        'department',
        'skill',
        'avatar',
    ]
    success_url = reverse_lazy('list-all-admin')

    #Interceptar los datos antes de ser guardados
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        first_n = request.POST['first_name']
        last_n = request.POST['last_name']
        """ form.full_name = first_n + ' ' + last_n
        form.save() """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #Para que no se guarde el registro se agrega commir=False
        employee = form.save(commit=False)
        employee.full_name = employee.first_name + ' ' + employee.last_name
        employee.save()
        return super(EmployeeUpdateView, self).form_valid(form)

class EmployeeDeleteView(DeleteView):
    template_name = 'employee/delete.html'
    model = Employee
    success_url = reverse_lazy('list-all-admin')