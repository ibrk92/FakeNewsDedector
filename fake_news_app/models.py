from django.db import models

class NewsArticle(models.Model):
    text = models.TextField()  # Artık sadece 'text' alanı mevcut
    is_fake = models.BooleanField(default=False)  # Haber sahte mi, değil mi onu belirtiyor

    def __str__(self):
        return self.text[:50]  # İlk 50 karakteri döndür


# Bu kisim kullanicidan gelen verileri kayit etmek icin