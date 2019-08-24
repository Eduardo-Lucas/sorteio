from import_export import resources

from apps.patrocinadores.models import Patrocinador


class PatrocinadorResource(resources.ModelResource):

    class Meta:
        model = Patrocinador
        fields = ('id', 'nome', )
