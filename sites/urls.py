from django.urls import path
from .views import home, site_detail

urlpatterns = [
    path("", home, name="home"),
    path("site/<int:site_id>/", site_detail, name="site_detail"),
]
