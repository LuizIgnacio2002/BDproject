# Generated by Django 5.1.3 on 2024-12-01 04:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_final', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estado', models.BooleanField()),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Gestor_de_invetario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='metodo_pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mozo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('capacidad', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('mozo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mozo')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('monto_devuelto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.factura')),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.metodo_pago')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='Pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido'),
        ),
        migrations.CreateModel(
            name='PedidoOferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.oferta')),
                ('Pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Gestor_de_invetario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.gestor_de_invetario')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
        ),
        migrations.CreateModel(
            name='OfertaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.oferta')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
        ),
        migrations.AddField(
            model_name='mozo',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rol'),
        ),
        migrations.AddField(
            model_name='gestor_de_invetario',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rol'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rol'),
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rol')),
            ],
        ),
        migrations.AddField(
            model_name='mozo',
            name='Trabajador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.trabajador'),
        ),
        migrations.AddField(
            model_name='gestor_de_invetario',
            name='Trabajador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.trabajador'),
        ),
        migrations.AddField(
            model_name='factura',
            name='Trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trabajador'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Trabajador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.trabajador'),
        ),
        migrations.CreateModel(
            name='Cajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rol')),
                ('Trabajador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('dni', models.CharField(max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='trabajador',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]
