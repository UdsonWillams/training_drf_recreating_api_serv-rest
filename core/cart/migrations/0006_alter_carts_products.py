# Generated by Django 3.2.6 on 2021-09-03 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_name'),
        ('cart', '0005_alter_carts_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='products',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]