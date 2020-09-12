from django.contrib import admin
from .models import Seferler

@admin.register(Seferler)
class SeferlerAdmin(admin.ModelAdmin):
    list_display = ["sofor","sofor_pilot","sefer_yeri", "ucret","firma","musteri","musteri_tel","musteri_adress","tarih", "ayar_tarih"]
    list_display_links = ["sofor","sofor_pilot","sefer_yeri", "ucret","firma","musteri","musteri_tel","musteri_adress","tarih", "ayar_tarih"]
    search_fields = ['sefer_yeri']
    list_filter = ['sofor']

    class Meta:
        model = Seferler
#class meta Seferler ile 5. satır 6. seferlerAdmini birleştirmemze yarıyor



