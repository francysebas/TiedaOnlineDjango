from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulo

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    if request.GET["producto"]:
        # mensaje = "Articulo buscado: %r" % request.GET["producto"]

        # variable que guarda el producto del html
        producto = request.GET["producto"]

        if len(producto)>20:
            mensaje = "Texto de búsqueda demaciado largo"

        else:
            articulos = Articulo.objects.filter(nombre__icontains=producto)

            return render(request, "resultado_busqueda.html", {"articulo": articulos, "query": producto})

    else:
        mensaje = "no has introducido ningun articulo"

    return HttpResponse(mensaje)

def contacto(request):
    if request.method == "POST":
        return render(request, "gracias.html")
    return render(request, "contacto.html")
