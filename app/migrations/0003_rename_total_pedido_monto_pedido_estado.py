# Generated by Django 5.1.3 on 2024-12-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_pedido_cliente_pedido_mesa_delete_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='total',
            new_name='monto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
