from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from api.views import getProd
# Create your views here.



def getProductos(request):
    return HttpResponse(getProd('0'))

def home(request):
    productos = getProd('0')  # Obtener todos los productos
    return render(request, 'front/index.html', {'productos': productos})

def product(request, id):
    productos = getProd(id)
    if productos:
        return render(request, 'front/producto.html', {'producto': productos})
    else:
        raise Http404("Producto no encontrado")