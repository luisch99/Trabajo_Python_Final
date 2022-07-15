# Generated by Django 4.0.6 on 2022-07-15 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLuis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesion', models.CharField(max_length=50)),
                ('Universidad', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Tipo', models.CharField(max_length=50)),
                ('Raza', models.CharField(max_length=50)),
            ],
        ),
    ]
