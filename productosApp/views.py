from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, ProductosTiendita
from .forms import UsuarioForm, ProductosTienditaForm

# Vistas para las páginas principales
def index(request):
    return render(request, 'productosApp/index.html')

def login(request):
    return render(request, 'productosApp/login.html')

def registro(request):
    return render(request, 'productosApp/registro.html')





# Vistas para mostrar productos
def ropadehombre(request):
    productos = ProductosTiendita.objects.all()
    context = {'productos': productos}
    return render(request, 'productosApp/ropadehombre.html', context)

def ropademujer(request):
    productos = ProductosTiendita.objects.all()
    context = {'productos': productos}
    return render(request, 'productosApp/ropademujer.html', context)

def joyeria(request):
    productos = ProductosTiendita.objects.all()
    context = {'productos': productos}
    return render(request, 'productosApp/joyeria.html', context)

# CRUD para usuarios

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista_usuarios')  
    else:
        form = UsuarioForm()
    return render(request, 'productosApp/registro.html', {'form': form})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'productosApp/crear_usuario.html', {'form': form})


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'productosApp/lista_usuarios.html', {'usuarios': usuarios})

def actualizar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'productosApp/actualizar_usuario.html', {'form': form, 'usuario': usuario})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'productosApp/eliminar_usuario.html', {'usuario': usuario})








# CRUD para productos sin terminar
def crear_producto(request):
    if request.method == 'POST':
        form = ProductosTienditaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductosTienditaForm()
    return render(request, 'productosApp/crear_producto.html', {'form': form})

def lista_productos(request):
    productos = ProductosTiendita.objects.all()
    return render(request, 'productosApp/lista_productos.html', {'productos': productos})

def actualizar_producto(request, pk):
    producto = get_object_or_404(ProductosTiendita, pk=pk)
    if request.method == 'POST':
        form = ProductosTienditaForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductosTienditaForm(instance=producto)
    return render(request, 'productosApp/actualizar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(ProductosTiendita, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productosApp/eliminar_producto.html', {'producto': producto})
