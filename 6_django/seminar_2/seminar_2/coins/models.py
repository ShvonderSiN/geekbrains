from django.db import models


class Coin(models.Model):
    CHOICES = [
        ('O', 'Орёл'),
        ('R', 'Решка'),
    ]
    result = models.CharField(max_length=1, choices=CHOICES)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.result} в {self.time}'

    @staticmethod
    def get_statistics(n) -> dict:
        """Статический метод для статистики по n последним броскам монеты"""
        n_total = Coin.objects.all().reverse()[:n]
        o_result = n_total.objects.filter(result='O').count()
        r_result = n_total.objects.filter(result='R').count()
        return {'Орел': o_result, 'Решка': r_result}
