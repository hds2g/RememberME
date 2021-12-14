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
        return obj.showing_date.strftime("%Y-%m-%d")

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
        "tag_list",
    )

    list_filter = ("tags",)
    search_fields = ["remember", "^user__username"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
