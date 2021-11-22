from django.contrib import admin
from . import models


class TagInline(admin.TabularInline):
    model = models.Tag


@admin.register(models.Remember)
class RememberAdmin(admin.ModelAdmin):

    """Remember Admin Definition"""

    inlines = (TagInline,)

    # list_display = ("__str__",)
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):

    """Tag Admin Definition"""

    list_display = ("__str__",)
