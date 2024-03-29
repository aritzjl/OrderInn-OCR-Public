# Generated by Django 4.2.1 on 2023-06-05 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('2', 'Equipamiento y accesorios'), ('3', 'Indumentaria y vestimenta'), ('5', 'Alimentación y suplementos'), ('6', 'Libros y material educativo')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Equ_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire_date', models.DateField(auto_created=True)),
                ('plan_type', models.CharField(choices=[('0', 'Ninguno'), ('1', 'Básico'), ('2', 'Medio'), ('3', 'Premium')], max_length=2, verbose_name='Plan')),
                ('expire_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.categoria_producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ficha_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.FileField(upload_to='images/products/services/')),
                ('image2', models.FileField(blank=True, upload_to='images/products/services/')),
                ('image3', models.FileField(blank=True, upload_to='images/products/services/')),
                ('image4', models.FileField(blank=True, upload_to='images/products/services/')),
                ('image5', models.FileField(blank=True, upload_to='images/products/services/')),
                ('status', models.CharField(choices=[('0', 'Sin estrenar'), ('1', 'Como nuevo'), ('2', 'Muy usado'), ('4', 'Roto')], max_length=50, verbose_name='Estado')),
                ('marca', models.CharField(choices=[('Ariat', 'Ariat'), ('Pessoa', 'Pessoa'), ('Eskadron', 'Eskadron'), ('Pikeur', 'Pikeur'), ('Animo', 'Animo'), ('Kingsland', 'Kingsland'), ('Samshield', 'Samshield'), ('Horseware', 'Horseware'), ('Charles Owen', 'Charles Owen'), ('Neue Schule', 'Neue Schule'), ('Stubben', 'Stubben'), ('Veredus', 'Veredus'), ('LeMieux', 'LeMieux'), ('Cavalleria Toscana', 'Cavalleria Toscana'), ('Horze', 'Horze'), ('Weatherbeeta', 'Weatherbeeta'), ('Woof Wear', 'Woof Wear'), ('Roeckl', 'Roeckl'), ('Tucci', 'Tucci'), ('Cavallo', 'Cavallo')], max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.categoria_producto')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.equ_plan')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.subcategoria_producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=180)),
                ('product_description', models.TextField(blank=True, default='')),
                ('product_type', models.CharField(choices=[('0', 'Caballo'), ('1', 'Producto'), ('2', 'Servicio')], max_length=2, verbose_name='Tipo de ficha')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
