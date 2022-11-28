from django.db import models

class Lunettes(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    prix = models.IntegerField(default=0)
    en_reduction = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', db_column='image', blank=True, null=True)

    def __str__(self):
        return self.nom
