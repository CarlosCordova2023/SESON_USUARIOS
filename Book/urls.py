from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', views.index, name='index'),  # Ruta principal que carga la vista index
    path('palindromo/<str:palabra>/', views.verificar_palindromo, name='verificar_palindromo'),
    path('palindromo/', views.verificar_palindromo_param, name='verificar_palindromo_param'),  # URL para procesar el palíndromo
    path('listbook/', views.listar_libros, name='listar_libros'),
    path('listbook/high/', views.listar_libros_valoracion, name='listar_libros_valoracion'),
    path('inputbook/', views.inputbook, name='inputbook'),
    path('success/', views.success, name='success'),
    path('registro/', views.registro, name='registro'),
    path('listar_libros/', views.listar_librosbd, name='listar_libros1'),
    #path('login/', views.login_view, name='login'),
    #path('logout/', views.logout_view, name='logout'),
    # Otras rutas de tu aplicación


    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('accounts/profile/', auth_views.LoginView.as_view(template_name='index.html'), name='inicio'),
    #path('login/', views.login_view, name='login'),


    #path('listbook/valoracion-alta/', views.libros_valoracion_alta, name='libros_valoracion_alta'),
    #path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    #path('cargar-libros-csv/', views.cargar_libros_csv, name='cargar_libros_csv'),

]
