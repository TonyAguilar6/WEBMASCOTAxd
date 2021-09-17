from django.db import models
# Create your models here.
class mascota(models.Model):
    pk_mascota = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)
    color = models.CharField(max_length=8, null=False, blank=False)
    age = models.CharField(max_length=2, null=False, blank=False)
    state = models.CharField(max_length=9, null=False, blank=False)
    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)


class client(models.Model):
    pk_client = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    tel = models.CharField(max_length=8, null=False, blank=False)
    direction = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)

class date(models.Model):
    pk_date = models.AutoField(primary_key=True, null=False, blank=False)
    fk_mascota = models.ForeignKey(mascota, null=False, blank=False, on_delete=models.CASCADE)
    fk_client = models.ForeignKey(client, null=False, blank=False, on_delete=models.CASCADE)
    day = models.CharField(max_length=8, null=False, blank=False)
    hour = models.CharField(max_length=5, null=False, blank=False)
    class Meta:
        verbose_name = 'date'
        verbose_name_plural = 'dates'
        ordering = ['day']

    def __str__(self):
        return "{0}".format(self.day)
