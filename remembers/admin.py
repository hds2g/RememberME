from django.contrib import admin
from . import models


@admin.register(models.Remember)
class RememberAdmin(admin.ModelAdmin):

    """Remember Admin Definition"""

    def created_format(self, obj):
        return obj.created.strftime("%Y-%m-%d")

    def updated_format(self, obj):
        return obj.updated.strftime("%Y-%m-%d")

    def showing_format(self, obj):
        return obj.updated.strftime("%Y-%m-%d")

    created_format.admin_order_field = "created"
    created_format.short_description = "CREATED"

    updated_format.admin_order_field = "updated"
    updated_format.short_description = "UPDATED"

    showing_format.admin_order_field = "showing_date"
    showing_format.short_description = "SHOWING DATE"

    list_display = (
        "__str__",
        "created_format",
        "updated_format",
        "showing_format",
        "stage",
    )

    list_filter = ("tags",)
    search_fields = ["remember", "^user__username"]
