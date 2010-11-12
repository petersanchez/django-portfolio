from django.conf import settings
from django.db import models


class ProjectActiveManager(models.Manager):
    def get_query_set(self):
        qs = super(ProjectActiveManager, self).get_query_set()
        return qs.filter(is_active=True)
