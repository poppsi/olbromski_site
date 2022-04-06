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
    path('systemy-mobilne', views.filtracja_systemy_mobilne, name='filtracja_systemy_mobilne_page'),
    path('filtry-magnetyczne-micromag', views.filtracja_filtry_magnetyczne_micromag, name='filtracja_filtry_magnetyczne_micromag_page'),
    path('wklady-filtracyjne-kleenoil', views.filtracja_wklady_filtracyjne_kleenoil, name='filtracja_wklady_filtracyjne_kleenoil_page'),
    path('badania-oleju', views.badania_oleju, name='badania_oleju_page'),
    path('sprzedaz-oleju', views.sprzedaz_oleju, name='sprzedaz_oleju_page'),
    path('kontakt', views.kontakt, name='kontakt_page'),
    path('dziekujemy', views.dziekujemy, name='dziekujemy_page'),
    # SEO pages
    path('filtracja-hydrauliczna', views.filtracja_hydrauliczna, name='filtracja_hydrauliczna'),
    path('srebrne-opilki-w-oleju', views.srebrne_opilki_w_oleju, name='srebrne_opilki_w_oleju'),
    path('zlote-opilki-w-oleju', views.zlote_opilki_w_oleju, name='zlote_opilki_w_oleju'),
    path('oczyszczanie-oleju-przepracowanego', views.oczyszczanie_oleju_przepracowanego, name='oczyszczanie_oleju_przepracowanego'),
    path('jak-oczyscic-olej-przepracowany', views.jak_oczyscic_olej_przepracowany, name='jak_oczyscic_olej_przepracowany'),
    path('jak-przefiltrowac-olej', views.jak_przefiltrowac_olej, name='jak_przefiltrowac_olej'),
    path('olej-hydrauliczny-jak-mleko', views.olej_hydrauliczny_jak_mleko, name='olej_hydrauliczny_jak_mleko'),
    path('agregat-do-filtracji-oleju-hydraulicznego', views.agregat_do_filtracji_oleju_hydraulicznego, name='agregat_do_filtracji_oleju_hydraulicznego'),
    path('opilki-w-oleju', views.opilki_w_oleju, name='opilki_w_oleju'),
    path('klasa-czystosci-oleju', views.klasa_czystosci_oleju, name='klasa_czystosci_oleju'),
    path('filtracja-oleju-przepracowanego', views.filtracja_oleju_przepracowanego, name='filtracja_oleju_przepracowanego')
]
