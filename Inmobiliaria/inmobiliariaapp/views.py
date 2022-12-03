from django.shortcuts import render
from inmobiliariaapp.models import Inmueble

# Create your views here.
def index(request):
    inmuebles=Inmueble.objects.all().order_by("Nombre")
    return render (request, "index.html", {"inmuebles": inmuebles})