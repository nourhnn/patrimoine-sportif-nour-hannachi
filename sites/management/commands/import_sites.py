import json
from django.core.management.base import BaseCommand
from sites.models import (
    Site,
    Olympiade,
    Typologie,
    Denomination,
    DateReference
)
from pathlib import Path


class Command(BaseCommand):
    help = "Import des sites sportifs depuis un fichier JSON"

    def handle(self, *args, **options):
        json_path = Path("data/sites-sportifs-emblematiques.json")

        if not json_path.exists():
            self.stdout.write(self.style.ERROR("Fichier JSON introuvable"))
            return

        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            # --- Olympiade (1-N)
            olympiade = None
            if item.get("site_olympique"):
                olympiade, _ = Olympiade.objects.get_or_create(
                    nom=item["site_olympique"]
                )

            # --- Site principal
            site = Site.objects.create(
                nom=item.get("nom", ""),
                adresse=item.get("adresse", ""),
                commune=item.get("commune", ""),
                departement=item.get("departement", ""),
                region=item.get("region", ""),
                description=item.get("description", ""),
                latitude=item.get("latitude"),
                longitude=item.get("longitude"),
                url_image=item.get("url_image", ""),
                site_olympique=olympiade
            )

            # --- Typologies (N-N)
            for t in item.get("typologie", []):
                typologie, _ = Typologie.objects.get_or_create(nom=t)
                site.typologies.add(typologie)

            # --- Denominations (N-N)
            for d in item.get("denomination", []):
                denomination, _ = Denomination.objects.get_or_create(nom=d)
                site.denominations.add(denomination)

            # --- Dates de référence (N-N)
            for dr in item.get("date_s_de_reference", []):
                date_ref, _ = DateReference.objects.get_or_create(valeur=dr)
                site.dates_reference.add(date_ref)

        self.stdout.write(self.style.SUCCESS("Import terminé avec succès ✅"))
