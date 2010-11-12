from django.contrib import admin
from portfolio.models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active',)
    list_editable = ('is_active',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(ProjectFile)
admin.site.register(ProjectImage)
