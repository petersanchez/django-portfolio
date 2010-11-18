from django.contrib import admin
from portfolio.models import *


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    fields = ('image', 'desc',)


class ProjectFileInline(admin.StackedInline):
    model = ProjectFile
    fields = ('file', 'desc',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active',)
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('name',),}
    inlines = (ProjectImageInline, ProjectFileInline)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}


class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProjectFile)
admin.site.register(ProjectImage)
