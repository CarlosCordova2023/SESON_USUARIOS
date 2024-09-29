

from django.http import HttpResponse

from .models import Libro
from django.shortcuts import render, redirect
#from .forms import LibroForm

import csv

from .forms import LibroForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')



""" def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página principal después de iniciar sesión
        else:
            # Agrega un mensaje de error si la autenticación falla
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    return render(request, 'login.html') """

""" @login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de login después de cerrar sesión
 """

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página principal después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})










# Simulación de libros en una lista de diccionarios
libros = [
    {'titulo': 'Libro A', 'autor': 'Autor A', 'valoracion': 1200, 'fecha_creacion': 'Sept. 28, 2024, 8:27 p.m.', 'fecha_modificacion': 'Sept. 28, 2024, 8:27 p.m.'},
    {'titulo': 'Libro B', 'autor': 'Autor B', 'valoracion': 1600, 'fecha_creacion': 'Sept. 28, 2024, 8:27 p.m.', 'fecha_modificacion': 'Sept. 28, 2024, 8:27 p.m.'},
    {'titulo': 'Libro C', 'autor': 'Autor C', 'valoracion': 1800, 'fecha_creacion': 'Sept. 28, 2024, 8:27 p.m.', 'fecha_modificacion': 'Sept. 28, 2024, 8:27 p.m.'},
]


def listar_libros(request):
    # Filtrar los libros con valoración mayor a 1500
    libros_filtrados = [libro for libro in libros if libro['valoracion'] > 1500]
    
    # Pasar ambas listas al template
    context = {
        'libros': libros,
        'libros_filtrados': libros_filtrados
    }
    
    return render(request, 'listar_libros.html', context)


def listar_librosbd(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros1.html', {'libros': libros})



def listar_libros_valoracion(request):
    # Filtrar los libros con valoración mayor a 1500
    libros_filtrados = [libro for libro in libros if libro['valoracion'] > 1500]
    return render(request, 'listar_libros_valoracion.html', {'libros': libros_filtrados})






""" def inputbook(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            # Aquí puedes manejar los datos del formulario, por ejemplo, guardarlos en la base de datos
            # libro = Libro.objects.create(**form.cleaned_data)
            return redirect('success')  # Redirigir a una página de éxito o a donde desees
    else:
        form = LibroForm()
    
    return render(request, 'inputbook.html', {'form': form}) """


@login_required
def inputbook(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirigir a una página de éxito o a donde desees
    else:
        form = LibroForm()
    
    return render(request, 'inputbook.html', {'form': form})


def success(request):
    return render(request, 'success.html')

def registro(request):
    return render(request, 'registro.html')

@login_required
def verificar_palindromo(request, palabra):
    # Limpiar la palabra/frase: eliminar espacios y convertir a minúsculas
    palabra_limpia = ''.join(e for e in palabra if e.isalnum()).lower()

    # Verificar si es un palíndromo
    es_palindromo = palabra_limpia == palabra_limpia[::-1]

    # Pasar los resultados a la plantilla
    return render(request, 'palindromo.html', {
        'palabra': palabra,
        'es_palindromo': es_palindromo
    })

def verificar_palindromo_param(request):
    palabra = request.GET.get('palabra', '')

    # Limpiar la palabra/frase: eliminar espacios y convertir a minúsculas
    palabra_limpia = ''.join(e for e in palabra if e.isalnum()).lower()

    # Verificar si es un palíndromo
    es_palindromo = palabra_limpia == palabra_limpia[::-1]

    # Pasar los resultados a la plantilla
    return render(request, 'palindromo.html', {
        'palabra': palabra,
        'es_palindromo': es_palindromo
    })