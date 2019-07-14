from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):  #models modulunden model i cagirdik
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar')
    title = models.CharField(max_length=120, verbose_name='Baslik')  #max length belirtmek zorundayiz. 120 karakter dedik
    content = models.TextField(verbose_name='Icerik')  #post metni
    crt_date = models.DateTimeField(verbose_name='Olusturma Tarihi')
    pub_date = models.DateTimeField(verbose_name="Yayim Tarihi", blank=True, null=True)  #yayim tarihi

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#verbase name ilgili kismin arayuzde nasil yazilacagini degistirir
#django'da nesne olusturmak icin class kullaniyoruz
#Post burada modelimizin ismi. class isimlerinin hep buyuk harfle basladigini unutma
#models.model ile django bu modelinn database e yazilmasi gerektigini anliyor.
#models.Foreignkey baska bir modele referans tannimliyormus.
###