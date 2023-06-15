from django.db import models
from config.settings import MEDIA_URL

class Imagenes(models.Model):
  nombre = models.CharField(max_length=100,verbose_name='Nombre',null=False,blank=False)
  imagen = models.ImageField(upload_to=f'{MEDIA_URL}imagenes/%Y/%m',null=False,blank=False)

  def __str__(self):
    return self.nombre