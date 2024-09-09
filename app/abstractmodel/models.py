from django.db import models

class TimestampableMixin(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField('Modificado em', auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
