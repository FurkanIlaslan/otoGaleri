from django.db import models

# Create your models here.
class Araclar(models.Model):
    resim1 = models.FileField(upload_to='araclar/', verbose_name="Araç Fotografı1", null=True)
    resim2 = models.FileField(upload_to='araclar/', verbose_name="Araç Fotografı2", null=True)
    resim3 = models.FileField(upload_to='araclar/', verbose_name="Araç Fotografı3", null=True)
    resim4 = models.FileField(upload_to='araclar/', verbose_name="Araç Fotografı4", null=True)
    resim5 = models.FileField(upload_to='araclar/', verbose_name="Araç Fotografı5", null=True)
    resim6 = models.FileField(upload_to='araclar/', verbose_name="Araç Fotografı6", null=True)
    resim7 = models.FileField(upload_to='araclar/', verbose_name="Araç Fotografı7", null=True)

    fiyat = models.IntegerField()
    marka = models.CharField(max_length=50)
    seri = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    yıl = models.CharField(max_length=20)
    yakit = models.CharField(max_length=50)
    vites = models.CharField(max_length=50)
    aracDurumu = models.CharField(max_length=50)
    km = models.CharField(max_length=50)
    kasaTipi = models.CharField(max_length=50)
    motorGucu = models.CharField(max_length=50)
    motorHacmi = models.CharField(max_length=50)
    cekisTipi = models.CharField(max_length=50)
    renk = models.CharField(max_length=50)

    def __str__(self):
        return self.marka


class Ekspertiz(models.Model):
    BOYA_SECENEKLERI = (
        ('Boyalı', 'Boyalı'),
        ('Degişen', 'Değişen'),
        ('Orijinal', 'Orijinal'),
    )
    arac = models.ForeignKey(Araclar, on_delete=models.CASCADE)

    resim = models.FileField(upload_to='araclar/', verbose_name="Ekpertiz Fotografı", null=True)

    sagOnCamurluk = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    arkaBagajKapagi = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    solArkaCamurluk = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    sagArkaKapi = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    sagOnKapi = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    tavan = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    solArkaKapi = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    solOnKapi = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    sagOnCamurluk = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    motorKaputu = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    motorHacmi = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    solOnCamurluk = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    onTampon = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    arkaTampon = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    sagMarspiyel = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)

    solMarspiyel = models.CharField(max_length = 50, choices=BOYA_SECENEKLERI)



class Donanım(models.Model):
    DONANIM_SECENEKLERİ = (
        ('Aktif Ön Koltuk Başlıkları', 'Aktif Ön Koltuk Başlıkları'),
        ('Merkezi Kilit', 'Merkezi Kilit'),
        ('Yükseklik Ayarlı Ön Emniyet Kemerleri', 'Yükseklik Ayarlı Ön Emniyet Kemerleri'),
        ('Merkezi Kilit', 'Merkezi Kilit'),
        ('Ayarlanabilir Direksiyon', 'Ayarlanabilir Direksiyon'),
        ('Elektrikli Ön Camlar', 'Elektrikli Ön Camlar'),
        ('Fonksiyonel Direksiyon', 'Fonksiyonel Direksiyon'),
        ('Hidrolik Direksiyon', 'Hidrolik Direksiyon'),
        ('Yol Bilgisayarı', 'Yol Bilgisayarı'),
        ('Klima (Analog)', 'Klima (Analog)'),
        ('Sunroof', 'Sunroof'),
        ('Arka Cam Buz Çözücü', 'Arka Cam Buz Çözücü'),
    )

    arac = models.ForeignKey(Araclar, on_delete=models.CASCADE, related_name = 'donanimlar')

    güvenlik1 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    güvenlik2 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    güvenlik3 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    güvenlik4 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    güvenlik5 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    güvenlik6 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)

    içDonanim1 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    içDonanim2 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    içDonanim3 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    içDonanim4 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    içDonanim5 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    içDonanim6 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)

    dişDonanim1 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    dişDonanim2 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    dişDonanim3 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    dişDonanim4 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    dişDonanim5 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)
    dişDonanim6 = models.CharField(max_length = 50, choices=DONANIM_SECENEKLERİ, blank=True, null=True)