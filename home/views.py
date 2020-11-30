from django.shortcuts import render
from . models import Test

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)

from . forms import TestForm

# Create your views here.

class ListTest(ListView):
    template_name = 'test.html'
    model = Test
    context_object_name = 'list'

class CreateViewTest(CreateView):
    template_name = 'add.html'
    model = Test
    form_class = TestForm
    """ fields = [
        'title',
        'subtitle',
        'quantity',
    ] """
    success_url = '/'


