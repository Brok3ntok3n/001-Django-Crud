from django.contrib import messages
from django.shortcuts import get_object_or_404,redirect , render

from .forms import ProductoForm
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            messages.success(
                request, f'El producto "{producto.nombre}" se creó correctamente.'
            )
            
            return redirect('productos:lista')
        messages.error(request, f'No se puede crear el producto. Revisa los errores del formulario.')
    else:
        form = ProductoForm()

    return render(request, 'productos/form.html', {
        'form': form,
        'titulo': 'Nuevo producto',
    })


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto = form.save()
            messages.success(
                request, f'El producto "{producto.nombre}" se actualizó correctamente.'
            )
            return redirect('productos:lista')
        messages.error(request, 'No se pudo actualizar el producto. Revisa los errores del formulario.')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/form.html', {
        'form': form,
        'titulo': 'Editar producto',
        'producto': producto,
    })
    
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'inactivar':
            producto.activo = False
            producto.save(update_fields=['activo', 'actualizado'])
            messages.warning(
                request, f'El producto "{producto.nombre}"  fue inactivado.'
            )
        elif accion == 'eliminar':
            nombre = producto.nombre
            producto.delete()
            messages.success(
                request, f'El producto "{nombre}" fue eliminado definitivamente'
            )
        else:
            messages.error(request, 'Accion no válida. No se realizó ningún cambio.')

        return redirect('productos:lista')

    return render(request, 'productos/confirmar_eliminar.html', {
        'producto': producto,
    })
