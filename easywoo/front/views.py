from django.shortcuts import render
from django.http import HttpResponse
from api.views import wcapi, getProd
# Create your views here.



def getProductos(request):
    return HttpResponse(getProd('0'))

def home(request):
    productos = getProd('0')  # Obtener todos los productos
    return render(request, 'front/index.html', {'productos': productos})
