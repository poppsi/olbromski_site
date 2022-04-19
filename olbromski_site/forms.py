from cProfile import label
from tkinter import Widget
from django import forms
from captcha.fields import ReCaptchaField 
from captcha.widgets import ReCaptchaV2Invisible

class ContactForm(forms.Form):
  client_name = forms.CharField(label='Imię', required=True, error_messages={"required":"Uzupełnij pole."})
  client_email = forms.EmailField(label='E-mail', required=True)
  client_message = forms.CharField(widget=forms.Textarea(), label='Wiadomość', required=True)
  captcha = ReCaptchaField(widget=ReCaptchaV2Invisible(api_params={'hl': 'pl'}), label="")