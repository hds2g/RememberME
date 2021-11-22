from django.contrib import admin
from . import models


@admin.register(models.Remember)
class RememberAdmin(admin.ModelAdmin):

    """Remember Admin Definition"""

    # list_display = ("__str__",)
    pass
