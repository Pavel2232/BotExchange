from django.contrib import admin

from exchange_rate.models import HistoryExchange, SubscriptionUser


# Register your models here.
@admin.register(HistoryExchange)
class HistoryExchangeAdmin(admin.ModelAdmin):
    pass


@admin.register(SubscriptionUser)
class SubscriptionUserAdmin(admin.ModelAdmin):
    pass
