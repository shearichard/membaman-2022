from django.contrib import admin

from .models import Organisation
from .models import SubOrganisation
from .models import Family
#from .models import Person
from .models import Caregiver
from .models import Member


admin.site.register(Organisation)
admin.site.register(SubOrganisation)
admin.site.register(Family)
#admin.site.register(Person)
admin.site.register(Caregiver)
admin.site.register(Member)
