"""olbromski_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home_page'),
    path('o-nas', views.o_nas, name='o_nas_page'),
    path('filtracja-oleju', views.filtracja_oleju, name='filtracja_oleju_page'),
    path('systemy-kleenoil', views.filtracja_systemy_kleenoil, name='filtracja_systemy_kleenoil_page'),
    path('system-kleenoil-typu-by-pass', views.filtracja_systemy_kleenoil_typu_by_pass, name='filtracja_systemy_kleenoil_typu_by_pass_page'),
    path('systemy-mobilne.html', views.filtracja_systemy_mobilne, name='filtracja_systemy_mobilne_page'),
    path('filtry-magnetyczne-micromag', views.filtracja_filtry_magnetyczne_micromag, name='filtracja_filtry_magnetyczne_micromag_page'),
    path('wklady-filtracyjne-kleenoil', views.filtracja_wklady_filtracyjne_kleenoil, name='filtracja_wklady_filtracyjne_kleenoil_page'),
    path('badania-oleju', views.badania_oleju, name='badania_oleju_page'),
    path('sprzedaz-oleju.html', views.sprzedaz_oleju, name='sprzedaz_oleju_page'),
    path('kontakt', views.kontakt, name='kontakt_page'),
    path('dziekujemy', views.dziekujemy, name='dziekujemy_page')
]
