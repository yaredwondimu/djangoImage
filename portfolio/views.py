from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html',{'projects':projects})