from django.contrib import admin
from .models import Birthday, Tag
empty_value_display = 'Не задано'


class BirthdayAdmin(admin.ModelAdmin):
    """Отображение админ-зоны постов."""

    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_editable = (
        'last_name',
        'birthday',
    )
    search_fields = ('first_name',)

    # @admin.display(description='текст')  # Декоратор, для корректного названия.
    # def short_text(self, obj):
    #     """Сокращение длины текста поста в админ-панели."""
    #     return (obj.text[:admin_text_length]
    #             + '..' if len(obj.text) > admin_text_length else obj.text)


class TagAdmin(admin.ModelAdmin):
    """Отображение админ-зоны постов."""

    list_display = (
        'tag',
    )

admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag, TagAdmin)
