"""p_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from home.views import ListTest, CreateViewTest
from django.conf import settings
from django.conf.urls.static import static
from employee.views import (
    HomeView,


    ListAllEmployees, 
    ListByArea, 
    ListBySearch,
    ListSkills,
    EmployeeDetailView,
    EmployeeCreateView,
    SuccessView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    ListAllEmployeesAdmin,
    )

from department.views import (
    NewDepartmentView,
    DepartmentListView,)

app_name = 'employee_app'


urlpatterns = [
    
    path('admin/', admin.site.urls),

    #home / employee
    path('',HomeView.as_view(),name='home'),
    path('list-all/', ListAllEmployees.as_view(), name='list-all'),
    path('detail-employee/<pk>/', EmployeeDetailView.as_view(), name='detail-employee'),

    #Listar empleados por area
    path('list-by-area/<shortname>', ListByArea.as_view(), name = 'list-by-area'),

    #Listar empleados admin
    path('list-all-admin/', ListAllEmployeesAdmin.as_view(), name = 'list-all-admin'),
    path('update/<pk>/', EmployeeUpdateView.as_view(), name = 'update'),
    path('delete/<pk>/', EmployeeDeleteView.as_view(), name = 'delete'),

    path('list/', ListTest.as_view()),
    path('add/', CreateViewTest.as_view(), name = 'add'),
   
    #Agregar empleado
    path('add-employee/', EmployeeCreateView.as_view(), name = 'add-employee'),

    path('list-by-search/', ListBySearch.as_view()),
    path('list-skills/', ListSkills.as_view()),
    path('success/', SuccessView.as_view(), name = 'success'),
    

    #Department
    path('new-department/', NewDepartmentView.as_view(), name = 'new-department'),
    path('list-departments/', DepartmentListView.as_view(), name = 'list-departments'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

