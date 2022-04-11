from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm


def home(request):
  form = ContactForm()

  context = {
    'form':form,
    'recaptcha_public_key':settings.RECAPTCHA_PUBLIC_KEY,
  }

  if request.method == "POST":
    form = ContactForm(request.POST)

    if form.is_valid():
      name = form.cleaned_data['client_name']
      email = form.cleaned_data['client_email']
      message = form.cleaned_data['client_message']

      send_mail(
        "Masz nowe zgłoszenie ze strony olbromski.pl", #Subject
        f"Imię: {name}\nE-mail: {email}\nWiadomość: {message}", #Message
        "olbromskipl@gmail.com", #From
        ["biuro@olbromski.pl", "olbromski.filip@gmail.com"], #To
        )
      return HttpResponseRedirect('dziekujemy')
  else:
    return render(request, 'index.html', context)

def o_nas(request):
  return render(request, 'o-nas.html')

def filtracja_oleju(request):
  return render(request, 'filtracja-oleju.html')

def filtracja_systemy_kleenoil(request):
  return render(request, 'systemy-kleenoil.html')

def filtracja_systemy_kleenoil_typu_by_pass(request):
  return render(request, 'system-kleenoil-typu-by-pass.html')

def filtracja_systemy_mobilne(reuqest):
  return render(reuqest, 'systemy-mobilne.html')

def filtracja_filtry_magnetyczne_micromag(request):
  return render(request, "filtry-magnetyczne-micromag.html")

def filtracja_wklady_filtracyjne_kleenoil(request):
  return render(request, 'wklady-filtracyjne-kleenoil.html')

def badania_oleju(request):
  return render(request, 'badania-oleju.html')

def sprzedaz_oleju(request):
  return render(request, 'sprzedaz-oleju.html')

def kontakt(request):
  form = ContactForm()

  context = {
    'form':form,
    'recaptcha_public_key':settings.RECAPTCHA_PUBLIC_KEY,
    'gmaps_api_key': settings.GOOGLE_MAPS_API_KEY,
  }

  if request.method == "POST":
    form = ContactForm(request.POST)

    if form.is_valid():
      name = form.cleaned_data['client_name']
      email = form.cleaned_data['client_email']
      message = form.cleaned_data['client_message']

      send_mail(
        "Masz nowe zgłoszenie ze strony olbromski.pl", #Subject
        f"Imię: {name}\nE-mail: {email}\nWiadomość: {message}", #Message
        "olbromskipl@gmail.com", #From
        ["biuro@olbromski.pl", "olbromski.filip@gmail.com"], #To
        )
      return HttpResponseRedirect('dziekujemy')
  else:
    return render(request, 'kontakt.html', context)

def dziekujemy(request):
  return render(request, 'dziekujemy.html')

# SEO pages
def filtracja_hydrauliczna(request):
  return render(request, 'filtracja-hydrauliczna.html')

def srebrne_opilki_w_oleju(request):
  return render(request, 'srebrne-opilki-w-oleju.html')

def zlote_opilki_w_oleju(request):
  return render(request, 'zlote-opilki-w-oleju.html')

def oczyszczanie_oleju_przepracowanego(request):
  return render(request, 'oczyszczanie-oleju-przepracowanego.html')

def jak_oczyscic_olej_przepracowany(request):
  return render(request, 'jak-oczyscic-olej-przepracowany.html')

def jak_przefiltrowac_olej(request):
  return render(request, 'jak-przefiltrowac-olej.html')

def olej_hydrauliczny_jak_mleko(request):
  return render(request, 'olej-hydrauliczny-jak-mleko.html')

def agregat_do_filtracji_oleju_hydraulicznego(request):
  return render(request, 'agregat-do-filtracji-oleju-hydraulicznego.html')

def opilki_w_oleju(request):
  return render(request, 'opilki-w-oleju.html')

def klasa_czystosci_oleju(request):
  return render(request, 'klasa-czystosci-oleju.html')

def filtracja_oleju_przepracowanego(request):
  return render(request, 'filtracja-oleju-przepracowanego.html')
