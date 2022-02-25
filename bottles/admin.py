# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Letter, Reply


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    """
    Admin class for the Letter model.
    """
    prepopulated_fields = {
        "slug": ("body",),
    }
    list_display = (
        "body",
        "author",
        "created_on"
        )
    search_fields = (
        "body",
        "topic"
        )


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    """
    Admin class for the Reply model.
    """
    list_display = (
        "name",
        "body",
        "letter",
        "created_on"
        )
    search_fields = (
        "body",
        "name"
        )
