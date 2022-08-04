from django.contrib import admin
from .models import Year
from .models import SubYear
from .models import Income
from .models import AccountEntry
from .models import AccountDebt
from .models import AccountPayment
from .models import ReferenceMapper


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('organisation', 'name', 'start', 'end')


@admin.register(AccountEntry)
class AccountEntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'member')


@admin.register(AccountDebt)
class AccountDebtAdmin(admin.ModelAdmin):
    list_display = ('invoice_reference',)


@admin.register(AccountPayment)
class AccountPaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'payment_reference', 'description', 'notes')


@admin.register(ReferenceMapper)
class ReferenceMapperAdmin(admin.ModelAdmin):
    list_display = ('payment_reference_used', 'payment_reference_intended', 'payment_origination_name')


@admin.register(SubYear)
class SubYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'start', 'end')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('subyear', 'member', 'received')
