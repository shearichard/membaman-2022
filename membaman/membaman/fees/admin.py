from django.contrib import admin
from .models import Year 
from .models import SubYear 
from .models import Income
from .models import AccountEntry
from .models import AccountDebt
from .models import AccountPayment
from .models import ReferenceMapper

class SubYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'start', 'end')

admin.site.register(Year)
admin.site.register(SubYear)
admin.site.register(Income)
admin.site.register(AccountEntry)
admin.site.register(AccountDebt)
admin.site.register(AccountPayment)
admin.site.register(ReferenceMapper)
