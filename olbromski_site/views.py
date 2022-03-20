from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def home(request):
  if request.method == "POST":
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    send_mail(
      "Masz nowe zgłoszenie ze strony olbromski.pl", #Subject
      f"Imię: {name}\nEmail: {email}\nWiadomość: {message}", #Message
      "olbromskipl@gmail.com", #From
      ["biuro@olbromski.pl", "olbromski.filip@gmail.com"], #To
      )

    return HttpResponseRedirect('dziekujemy')
  else:
    return render(request, 'index.html')

    

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
  if request.method == "POST":
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    send_mail(
      "Masz nowe zgłoszenie ze strony olbromski.pl", #Subject
      f"Imię: {name}\nEmail: {email}\nWiadomość: {message}", #Message
      "olbromskipl@gmail.com", #From
      ["biuro@olbromski.pl", "olbromski.filip@gmail.com"], #To
      )
      
    return HttpResponseRedirect('dziekujemy')
  else:
    return render(request, 'kontakt.html')

def dziekujemy(request):
  return render(request, 'dziekujemy.html')
