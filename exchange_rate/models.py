from django.db import models


class HistoryExchange(models.Model):
    user_id_tg = models.BigIntegerField(verbose_name='ID пользоваталя Tg')
    rate = models.FloatField(verbose_name='Курс доллара')
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'История обмена'
        verbose_name_plural = 'Истории обмена'

    def __str__(self):
        return str(self.user_id_tg)


class SubscriptionUser(models.Model):
    user_id_tg = models.BigIntegerField(verbose_name='ID пользоваталя Tg', unique=True)
    subscription_on = models.BooleanField(default=False, verbose_name='Подписка')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return '{} {}'.format(str(self.user_id_tg), self.subscription_on)
