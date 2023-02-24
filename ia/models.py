from django.db import models

class Referencia(models.Model):
    arquivo_ia = models.FileField(null=True, blank=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self) -> str:
        return self.titulo
