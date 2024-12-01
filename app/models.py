from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # a credit attribute with 7 decimal
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    dni = models.CharField(max_length=8)
    
    def __str__(self):
        return self.nombre
    
class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Trabajador(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.nombre
    
class Cajero(models.Model):
    Trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Trabajador.user.nombre
    
class Cliente(models.Model):
    Trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Trabajador.user.nombre
    
class Mozo(models.Model):
    Trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Trabajador.user.nombre
    
class Gestor_de_invetario(models.Model):
    Trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Trabajador.user.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Gestor_de_invetario = models.ForeignKey(Gestor_de_invetario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Oferta(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    def __str__(self):
        return self.nombre
    
class OfertaProducto(models.Model):
    Oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Oferta.nombre
    
class Pedido(models.Model):
    fecha = models.DateField()
    total = models.DecimalField(max_digits=5, decimal_places=2)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.fecha)
    

    
