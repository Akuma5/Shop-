from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
from django.utils.safestring import mark_safe

from .models import Magazine, Category, MagazineImage


class ImageAdminInline(TabularInline):
    extra = 1
    model = MagazineImage


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image_show', 'price', 'cat', 'is_published', 'id']
    list_editable = ['price', 'cat', ]
    list_display_links = ['id', 'title', 'id', 'image_show', 'content']
    search_fields = ['id', 'title']
    ordering = ['-title', '-price']
    list_filter = ['is_published', 'time_create']
    list_per_page = 10
    inlines = (ImageAdminInline,)

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"
    image_show.__name__ = "Картинка"


# admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Category)




# @admin.register(Magazine)
# class ProductModelAdmin(ModelAdmin):
#     inlines = (ImageAdminInline, )
#
#     fields = (
#         '__all__',
#     )



