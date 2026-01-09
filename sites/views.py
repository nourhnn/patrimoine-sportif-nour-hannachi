from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Site
from django.shortcuts import get_object_or_404


def home(request):
    # Récupérer tous les sites
    sites = Site.objects.all().order_by("nom")

    # Pagination : 12 sites par page
    paginator = Paginator(sites, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "sites/home.html", {
        "page_obj": page_obj
    })


def site_detail(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    return render(request, "sites/detail.html", {
        "site": site
    })
