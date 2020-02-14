from django.db import models

class Seferler(models.Model):
    sofor = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Admin')
    sofor_pilot = models.CharField(max_length=30, verbose_name="Şöför İsmi", null=True)
    sefer_yeri = models.CharField(max_length=60, verbose_name='Transfer Yeri')
    ucret = models.IntegerField(verbose_name='Ücret')
    firma = models.CharField(max_length=100, verbose_name="Firma Adı", null=True)
    musteri = models.CharField(max_length=100, verbose_name='Müşteri Adı')
    musteri_adress = models.CharField(max_length=200, verbose_name='Müşterinin Adresi',null=True)
    tarih = models.DateTimeField(auto_now_add=True, verbose_name='Transfer Tarihi')

    def __str__(self):
        return self.firma

class Chart(models.Model):
    title = models.CharField(max_length=50, verbose_name="",null=True)
    fiyat = models.CharField(max_length=50, verbose_name="Fiyat",null=True)
    yas = models.CharField(max_length=50, verbose_name="Yaşı",null=True)

