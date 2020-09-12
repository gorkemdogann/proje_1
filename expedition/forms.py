from django import forms
from .models import Seferler

class ExpeditionForm(forms.ModelForm):
    class Meta:
        model=Seferler
        fields = ["sofor","sofor_pilot","sefer_yeri","ucret","firma","musteri","musteri_tel","musteri_adress","ayar_tarih"]
