from django.db import models

# Create your models here.

class CV(models.Model):
    titre = models.CharField(max_length=255, default="mon_cv")
    fichier = models.FileField(upload_to='media/')
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
