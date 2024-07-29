from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from ashop.apps.catalog.models import Category


# Register your models here.


class CategoryMyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Category, CategoryMyAdmin)
