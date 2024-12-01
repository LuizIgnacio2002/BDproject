from django.contrib import admin
from .models import Usuario, Rol, Trabajador, Cajero, Cliente, Mozo, Gestor_de_invetario, Categoria, Producto, Oferta, OfertaProducto, Pedido, PedidoOferta, PedidoProducto, Mesa, Factura, metodo_pago, Pago

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'dni')
    search_fields = ('nombre', 'apellido', 'correo', 'dni')
    list_filter = ('nombre', 'apellido', 'correo', 'dni')
    
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rol')
    search_fields = ('user', 'rol')
    list_filter = ('user', 'rol')
    
class CajeroAdmin(admin.ModelAdmin):
    list_display = ('Trabajador', 'rol')
    search_fields = ('Trabajador', 'rol')
    list_filter = ('Trabajador', 'rol')
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Trabajador', 'rol')
    search_fields = ('Trabajador', 'rol')
    list_filter = ('Trabajador', 'rol')
    
class MozoAdmin(admin.ModelAdmin):
    list_display = ('Trabajador', 'rol')
    search_fields = ('Trabajador', 'rol')
    list_filter = ('Trabajador', 'rol')
    
class Gestor_de_invetarioAdmin(admin.ModelAdmin):
    list_display = ('Trabajador', 'rol')
    search_fields = ('Trabajador', 'rol')
    list_filter = ('Trabajador', 'rol')
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    search_fields = ('nombre', 'precio', 'stock', 'categoria')
    list_filter = ('nombre', 'precio', 'stock', 'categoria')
    
class OfertaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'descuento')
    search_fields = ('nombre', 'fecha_inicio', 'fecha_fin', 'descuento')
    
class OfertaProductoAdmin(admin.ModelAdmin):
    list_display = ('Oferta', 'Producto')
    search_fields = ('Oferta', 'Producto')
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('total',)
    search_fields = ('total',)
    
class PedidoOfertaAdmin(admin.ModelAdmin):
    list_display = ('Pedido', 'Oferta')
    search_fields = ('Pedido', 'Oferta')
    
class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = ('Pedido', 'Producto')
    search_fields = ('Pedido', 'Producto')
    
class MesaAdmin(admin.ModelAdmin):
    list_display = ('capacidad',)
    
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('Pedido',)
    
class metodo_pagoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    
class PagoAdmin(admin.ModelAdmin):
    list_display = ('Factura', 'metodo_pago')
    search_fields = ('Factura', 'metodo_pago')
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Cajero, CajeroAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Mozo, MozoAdmin)
admin.site.register(Gestor_de_invetario, Gestor_de_invetarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(OfertaProducto, OfertaProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoOferta, PedidoOfertaAdmin)
admin.site.register(PedidoProducto, PedidoProductoAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(metodo_pago, metodo_pagoAdmin)
admin.site.register(Pago, PagoAdmin)



