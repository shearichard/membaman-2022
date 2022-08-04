from django.contrib import admin

from .models import Organisation
from .models import SubOrganisation
from .models import Family
from .models import Caregiver
from .models import Member


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'postal_address')


@admin.register(SubOrganisation)
class SubOrganisationAdmin(admin.ModelAdmin):
    list_display = ('sub_name', 'organisation')


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'suburb', 'city', 'phone_fixed')


@admin.register(Caregiver)
class CaregiverAdmin(admin.ModelAdmin):
    list_display = ('family', 'relationship', 'phone_mobile', 'email')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('organisation', 'sub_organisation', 'name_family', 'name_given', 'family')
