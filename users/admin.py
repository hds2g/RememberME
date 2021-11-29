from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from remembers import models as remembers_model


class RememberInline(admin.TabularInline):
    model = remembers_model.Remember


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    inlines = [
        RememberInline,
    ]

    # overide UserAdmin
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
