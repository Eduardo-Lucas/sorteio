from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.cadastros.models import Cadastro


@admin.register(Cadastro)
class CadastroResource(ImportExportModelAdmin):
    pass
