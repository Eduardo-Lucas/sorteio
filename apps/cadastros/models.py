import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Cadastro(models.Model):
    nome_completo = models.CharField(max_length=50, unique=True,
                                     help_text='Informe seu nome completo')
    email = models.EmailField(max_length=50, unique=True,
                              help_text='Informe seu endereço de E-mail')
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    codigo = models.UUIDField(primary_key=False
                              , default=uuid.uuid4, editable=False)
    leitura = models.BooleanField(default=False, )
    
    def __str__(self):
        return self.nome_completo
    
    def get_absolute_url(self):
        return reverse('cadastro_detail', args={self.id})
    
    def clean(self):
        """Se o valor do campo leitura não for marcado, exibe a mensagem de erro e não deixa gravar"""
        if not self.leitura:
            raise ValidationError({'leitura': _('Confirme que leu o Regulamento e a Política de Privacidade.')})
        
    class Meta:
        ordering = ['nome_completo']
