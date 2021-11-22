from django.contrib import admin
from . import models


@admin.register(models.Remember)
class RememberAdmin(admin.ModelAdmin):

    """Remember Admin Definition"""

    def created_format(self, obj):
        return obj.created.strftime("%Y-%m-%d")

    def updated_format(self, obj):
        return obj.updated.strftime("%Y-%m-%d")

    created_format.admin_order_field = "created"
    created_format.short_description = "CREATED"

    updated_format.admin_order_field = "updated"
    updated_format.short_description = "UPDATED"

    list_display = (
        "__str__",
        "created_format",
        "updated_format",
        "showing_date",
        "stage",
    )
    pass
