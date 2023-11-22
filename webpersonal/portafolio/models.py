from operator import truediv
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.

class project(models.Model):
    title=models.CharField(max_length=200,verbose_name='Titulo')
    descripcion=models.TextField(verbose_name='Descripción')
    image=models.ImageField(verbose_name='Imagen')
    link=models.URLField(null=True,blank=True,verbose_name='Dirección web')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Creación')
    updated=models.DateTimeField(auto_now=True,verbose_name='Actualización')

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        ordering=['-created']

    def __str__(self):
        return f'{self.title}'
