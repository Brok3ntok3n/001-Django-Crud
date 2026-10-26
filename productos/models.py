from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.CharField(blank=True, verbose_name='Descripción')
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio'
    )
    stock = models.PositiveIntegerField(default=0, verbose_name='Stock')
    imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True,
        verbose_name='Imagen',
    )
    activo = models.BooleanField(default=True, verbose_name='Activo')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Actualizado')


    class Meta:
        ordering = ['-creado']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre