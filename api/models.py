from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    estado = models.BooleanField()
    departamento = ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    ciudad = ForeignKey(Ciudad, on_delete=models.CASCADE)
    correo = models.EmailField()
    genero = models.CharField(max_length=1)
    avatar = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombres


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    detalle = models.CharField(max_length=50)
    categoria = ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre


class Boleta(models.Model):
    usuario = ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField("date published")
    detalle = models.CharField(max_length=50)
    total = models.FloatField()

    def __str__(self):
        return self.usuario


class Extra(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre


class DetalleProducto(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto.nombre


class DetalleExtra(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.boleta.usuario.nombres
