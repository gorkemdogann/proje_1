from django.db import models

class Seferler(models.Model):
    sofor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, verbose_name='Admin')
    sofor_pilot = models.CharField(max_length=30, verbose_name="Şoför İsmi", null=True)
    sefer_yeri = models.CharField(max_length=60, verbose_name='Transfer Yeri')
    ucret = models.IntegerField(verbose_name='Ücret')
    firma = models.CharField(max_length=100, verbose_name="Firma Adı", null=True)
    musteri = models.CharField(max_length=100, verbose_name='Misafir Adı')
    musteri_tel = models.IntegerField(verbose_name='Misafir Telefon No',null=True)
    musteri_adress = models.CharField(max_length=200, verbose_name='Misafir Adresi',null=True)
    tarih = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    ayar_tarih = models.DateTimeField(auto_now_add=False, verbose_name='Transfer Tarih-Saati',null=True)

    def __str__(self):
        return self.firma

class Firma(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Firma Adı")
    tel_no = models.CharField(max_length=15, verbose_name="Firma Tel.")
    adres = models.CharField(max_length=200, verbose_name='Firma Adresi')

    class Meta:
        db_table='tbl_firma' # Veritabanında bulunan tablo adını belirtir.

class Musteri(models.Model):
    id = models.AutoField(primary_key=True)
    firma = models.ForeignKey(Firma, models.DO_NOTHING)
    name = models.CharField(max_length=50, verbose_name='Misafir Adı')
    tel_no = models.CharField(max_length=15, verbose_name='Misafir Tel.')
    adres = models.CharField(max_length=200, verbose_name='Misafir Adresi')

    class Meta:
        db_table='tbl_musteri'

class Tarih(models.Model):
    id = models.AutoField(primary_key=True)
    tarih = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    ayar_tarih = models.DateTimeField(auto_now_add=False, verbose_name='Transfer Tarih-Saati')

class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    sofor = models.ForeignKey(Transfer, models.DO_NOTHING)
    plaka = models.ForeignKey(Transfer, models.DO_NOTHING)
    arac = models.ForeignKey(Transfer, models.DO_NOTHING)
    sofor = models.CharField(max_length=30, verbose_name="Şoför İsmi", null=True)
    plaka = models.CharField(max_length=30, verbose_name="Palaka", null=True)
    ucret = models.IntegerField(verbose_name='Ücret')

