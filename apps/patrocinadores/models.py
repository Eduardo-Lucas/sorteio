from django.db import models


class Patrocinador(models.Model):
    nome = models.CharField(max_length=50, unique=True, help_text='Indica o Nome do Patrocinador')
    logo = models.ImageField(upload_to='patrocinadores', blank=True)
    ativo = models.BooleanField(default=True, help_text='Indica se o Patrocinador está ativo ou não')
