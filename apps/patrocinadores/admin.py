from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.patrocinadores.models import Patrocinador


@admin.register(Patrocinador)
class PatrocinadorResource(ImportExportModelAdmin):
    pass
