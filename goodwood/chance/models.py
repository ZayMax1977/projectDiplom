from django.db import models


class Chance(models.Model):
    number_phone = models.CharField(max_length=20, default="",verbose_name = "Номер победителя")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата выигрыша")


    def __str__(self):
        return self.number_phone

    class Meta:
        verbose_name = "Победитель"
        verbose_name_plural = "Победители"
        ordering = ['-created_at', 'number_phone']
