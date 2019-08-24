from django.db import models
from django.urls import reverse


class Patrocinador(models.Model):
    nome = models.CharField(max_length=50, unique=True, help_text='Indica o Nome do Patrocinador')
    logo = models.ImageField(upload_to='patrocinadores', blank=True)
    ativo = models.BooleanField(default=True, help_text='Indica se o Patrocinador está ativo ou não')

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('patrocinador_detail', args={self.id})

    class Meta:
        ordering = ['nome']
        verbose_name = 'Patrocinador'
        verbose_name_plural = 'Patrocinadores'
