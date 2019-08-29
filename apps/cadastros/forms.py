from django.forms import ModelForm, forms
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
            msg = 'Confirme que leu o Regulamento e a Política de Privacidade.'
            self.add_error('leitura', msg)
            # raise forms.ValidationError({'leitura': 'Confirme que leu o Regulamento e a Política de Privacidade.'})