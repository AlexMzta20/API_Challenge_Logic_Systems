from django.db import models  # Importa el módulo models de Django.

# Create your models here. Aquí es dónde debemos crear los modelos.
# Se manejó un modelo correspondiente a los datos de un programador.
# Descripción de los campos del modelo.
# User -> ID(AutoField), Fullname(CharField), Nickname(CharField), Gender(CharFiel), Age (IntegerField), Is Active(BooleanField).


# Define una clase Programmer que hereda de models.Model.
class Programmer(models.Model):
    # Define un campo id que es una clave primaria y se autoincrementa.
    id = models.AutoField(primary_key=True)
    # Define un campo fullname que es un campo de caracteres con una longitud máxima de 100.
    fullname = models.CharField(max_length=100)
    # Define un campo nickname que es un campo de caracteres con una longitud máxima de 50.
    nickname = models.CharField(max_length=50)
    # Define un campo gender que es un campo de caracteres con una longitud máxima de 10.
    gender = models.CharField(max_length=10)
    # Define un campo age que es un campo entero positivo pequeño.
    age = models.PositiveSmallIntegerField()
    # Define un campo is_active que es un campo booleano con un valor predeterminado de True.
    is_active = models.BooleanField(default=True)
