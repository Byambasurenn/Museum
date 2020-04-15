from django.db import models

class Exhibit(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nfc_id = models.CharField(max_length=30, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    title_en = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    description_en = models.TextField(blank=True, default='')
    image = models.CharField(max_length=100, blank=True, default='')
    audio = models.FileField(upload_to='audio/', blank=True)
    audio_en = models.FileField(upload_to='audio/en/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
