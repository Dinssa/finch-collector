from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    finches = Finch.objects.all()
    return render(request, 'finch/index.html', {'finches': finches})

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finch/detail.html', {'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finch/{finch.id}'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'species', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'