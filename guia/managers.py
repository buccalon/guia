from django.db import models


class DraftManager(models.Manager):
    def published(self):
        queryset = super().get_queryset()
        return queryset.filter(is_draft=False)
