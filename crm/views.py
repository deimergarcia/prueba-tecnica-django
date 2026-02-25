import requests
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cliente, Oportunidad
from .forms import ClienteForm, OportunidadForm

def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('-fecha_registro')
    frase = None
    try:
        response = requests.get('https://zenquotes.io/api/random', timeout=5)
        if response.status_code == 200:
            data = response.json()
            frase = f"“{data[0]['q']}” — {data[0]['a']}"

    except Exception as e:
        frase = "“El éxito es la suma de pequeños esfuerzos repetidos día tras día.” — Robert Collier"
    return render(request, 'crm/lista_clientes.html', {'clientes': clientes,
        'frase': frase})

def crear_cliente(request):
    ciudades = []
    error_api = None
    try:
        response = requests.get('https://api-colombia.com/api/v1/City', timeout=5)
        if response.status_code == 200:
            data = response.json()
            ciudades = [ciudad['name'] for ciudad in data if ciudad.get('name')]
            ciudades.sort() 
        else:
            error_api = f"Error al obtener ciudades: {response.status_code}"
    except Exception as e:
        error_api = "No fue posible conectar con la API de ciudades de Colombia."

    if request.method == 'POST':
        form = ClienteForm(request.POST, ciudades=ciudades)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('lista_clientes')
    else:
        form = ClienteForm(ciudades=ciudades)

    return render(request, 'crm/form_cliente.html', {
        'form': form,
        'titulo': 'Crear Cliente',
        'error_api': error_api
    })

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    # Reutilizamos la lógica de consumo de API
    ciudades = []
    error_api = None
    try:
        response = requests.get('https://api-colombia.com/api/v1/City', timeout=5)
        if response.status_code == 200:
            data = response.json()
            ciudades = [ciudad['name'] for ciudad in data if ciudad.get('name')]
            ciudades.sort()
        else:
            error_api = "Error al obtener ciudades."
    except Exception as e:
        error_api = "No fue posible conectar con la API."

    if request.method == 'POST':
        form = ClienteForm(request.POST, ciudades=ciudades, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado.')
            return redirect('lista_clientes')
    else:
        form = ClienteForm(ciudades=ciudades, instance=cliente)

    return render(request, 'crm/form_cliente.html', {
        'form': form,
        'titulo': 'Editar Cliente',
        'error_api': error_api
    })

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado.')
        return redirect('lista_clientes')
    return render(request, 'crm/confirmar_eliminar.html', {'objeto': cliente, 'tipo': 'cliente'})

def crear_oportunidad(request):
    if request.method == 'POST':
        form = OportunidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oportunidad creada.')
            return redirect('lista_clientes')
    else:
        form = OportunidadForm()
    return render(request, 'crm/form_oportunidad.html', {'form': form, 'titulo': 'Crear Oportunidad'})

def editar_oportunidad(request, pk):
    oportunidad = get_object_or_404(Oportunidad, pk=pk)
    if request.method == 'POST':
        form = OportunidadForm(request.POST, instance=oportunidad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oportunidad actualizada.')
            return redirect('lista_clientes')
    else:
        form = OportunidadForm(instance=oportunidad)
    return render(request, 'crm/form_oportunidad.html', {'form': form, 'titulo': 'Editar Oportunidad'})

def eliminar_oportunidad(request, pk):
    oportunidad = get_object_or_404(Oportunidad, pk=pk)
    if request.method == 'POST':
        oportunidad.delete()
        messages.success(request, 'Oportunidad eliminada.')
        return redirect('lista_clientes')
    return render(request, 'crm/confirmar_eliminar.html', {'objeto': oportunidad, 'tipo': 'oportunidad'})

def ver_oportunidades(request):
    # Obtener solo clientes que tengan al menos una oportunidad
    clientes_con_oportunidades = Cliente.objects.filter(
        oportunidad__isnull=False
    ).distinct().order_by('nombre_completo')

    return render(request, 'crm/ver_oportunidades.html', {
        'clientes': clientes_con_oportunidades
    })

