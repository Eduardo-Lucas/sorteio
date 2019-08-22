from import_export import resources

from apps.cadastros.models import Cadastro


class CadastroResource(resources.ModelResource):

    class Meta:
        model = Cadastro
        fields = ('id', 'nome_completo', 'email', 'telefone', )
