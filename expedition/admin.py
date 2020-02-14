from django.contrib import admin
from .models import Seferler

@admin.register(Seferler)
class SeferlerAdmin(admin.ModelAdmin):
    list_display = ["sofor", "sefer_yeri", "ucret", "tarih", "firma", "musteri"]
    list_display_links = ["sofor", "sefer_yeri", "ucret", "tarih", "firma", "musteri"]
    search_fields = ['sefer_yeri']
    list_filter = ['sofor']

    class Meta:
        model = Seferler
#class meta Seferler ile 5. satır 6. seferlerAdmini birleştirmemze yarıyor



