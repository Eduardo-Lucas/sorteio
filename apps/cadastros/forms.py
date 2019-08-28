from django.forms import ModelForm
from django.core.exceptions import ValidationError
from apps.cadastros.models import Cadastro


class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome_completo', 'email', 'telefone', 'leitura']

    def clean(self):
        """Se o valor do campo leitura não for marcado, exibe a mensagem de erro e não deixa gravar"""
        cleaned_data = super().clean()
        leitura = cleaned_data.get("leitura")
        if not leitura:
            raise ValidationError({'leitura': 'Confirme que leu o Regulamento e a Política de Privacidade.'})