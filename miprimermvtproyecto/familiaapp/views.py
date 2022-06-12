from django.shortcuts import render
from .models import Familiares

# Create your views here.
def familias (request):
    familias_list = Familiares.objects.all ()
    return render(request,'familiaapp.html', {'familias' : familias_list})
