from django.db import models


class Track(models.Model):
    name = models.CharField(verbose_name='Name', max_length=128, unique=True)
    streaming_link = models.CharField(verbose_name='Stream', max_length=256, blank=True)
    link_to_aj = models.CharField(verbose_name='aj_link', max_length=256, blank=True)
    download_link = models.FileField(upload_to='tracks/')
    download_counter = models.PositiveIntegerField(default='0')
    play_counter = models.PositiveIntegerField(default='0')
    MAIN_GENRE = (
        ('Epic', 'Epic'),
        ('Upbeat', 'Upbeat'),
        ('Abstract', 'Abstract'),
        ('Sport', 'Sport'),
        ('Corporate', 'Corporate'),
    )
    genre = models.CharField(verbose_name='Genre', max_length=256, choices=MAIN_GENRE)
    mood = models.CharField(verbose_name='Mood', max_length=256, blank=True)
