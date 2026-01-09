from django.db import models

class Olympiade(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Typologie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Denomination(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class DateReference(models.Model):
    valeur = models.CharField(max_length=50)

    def __str__(self):
        return self.valeur

class Site(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255, blank=True)
    commune = models.CharField(max_length=100, blank=True)
    departement = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)

    description = models.TextField(blank=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    url_image = models.URLField(blank=True)

    # Relations
    site_olympique = models.ForeignKey(
        Olympiade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sites"
    )

    typologies = models.ManyToManyField(Typologie, blank=True)
    denominations = models.ManyToManyField(Denomination, blank=True)
    dates_reference = models.ManyToManyField(DateReference, blank=True)

    def __str__(self):
        return self.nom
