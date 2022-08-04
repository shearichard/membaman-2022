from django.db import models

from members.models import Organisation
from members.models import Member


class Year(models.Model):
    '''
    A `Year` models a single year
    of an `Organisation` activity

    '''
    class Meta:
        ordering = ['start', 'end']

    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()

    def __unicode__(self):
        return str(self.name) + str(' (') + str(self.organisation.name) + str(')')

    def __str__(self):
        return "{} ({})".format(self.name, self.organisation.name)


class SubYear(models.Model):
    '''
    A fraction of the `Year` model

    There should be sufficient `SubYear`
    instances with suitable start end
    dates so that the whole year is covered
    with no gaps.

    In some cases a SubYear will be a 1-1
    with Year depending on how the `Organisation`
    does their billing.

    '''
    class Meta:
        ordering = ['year__organisation__name', 'start', 'end']

    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()

    def year_name(self):
        return self.year.name
    year_name.short_description = 'Year Name'

    def organisation_name(self):
        return self.year.organisation
    organisation_name.short_description = 'Organisation Name'

    def __unicode__(self):
        return str(self.name) + str(' (') + str(self.year.organisation.name) + str(' - ') + str(self.year.name) + str(')')

    def __str__(self):
        return "{}/{}".format(self.name, self.year)


class Income(models.Model):
    '''
    `Income` represents the income from a `Member`
    based for a given `SubYear`

    Initially the model will just be a string
    to contain the non-numeric values that have
    been entered into the data that's being converted
    from but in the longer term this model will take
    on a more typed form
    '''
    class Meta:
        ordering = ['member__name_family', 'member__name_given', 'subyear__start', 'subyear__end']

    subyear = models.ForeignKey(SubYear, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    received = models.CharField(max_length=100)

    def year_name(self):
        return self.subyear.year.name
    year_name.short_description = 'Year Name'

    def subyear_name(self):
        return self.subyear.name
    subyear_name.short_description = 'Sub-Year Name'

    def __unicode__(self):
        return str(' (') + str(self.subyear.year.name) + str(' - ') + \
            str(self.subyear.name) + str(':') + str(self.member) + \
            str(')') + " " + str(self.received)

    def __str__(self):
        return self.__unicode__()


class AccountEntry(models.Model):
    '''
    `AccountEntry` represents either a debt or a
    credit. We record membership payments which
    have been asked for via `AccountEntry` and we
    record amounts received via `AccountEntry`

    '''
    DEBT = 'DT'
    CREDIT = 'CR'

    ACCOUNT_ENTRY_TYPE_CHOICES = (
        (DEBT, 'Debt'),
        (CREDIT, 'Credit')
    )
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()


class AccountDebt(AccountEntry):
    invoice_reference = models.CharField(max_length=10)


class AccountPayment(AccountEntry):

    AUTOPAYMENT = 'AT'
    BANKTRANSFER = 'TR'
    CASH = 'CA'
    CHEQUE = 'CH'
    DISCOUNT = 'DI'
    OTHER = 'OT'

    PAYMENT_TYPE_CHOICES = (
        (AUTOPAYMENT, 'Automated Payment'),
        (BANKTRANSFER, 'Bank Transfer'),
        (CASH, 'Cash'),
        (CHEQUE, 'Credit'),
        (DISCOUNT, 'Discount'),
        (OTHER, 'Other'),
    )
    payment_type = models.CharField(max_length=2,
                                    choices=PAYMENT_TYPE_CHOICES,
                                    default=OTHER)
    payment_reference = models.CharField(max_length=10)
    description = models.CharField(max_length=128, null=True, blank=True)
    notes = models.CharField(max_length=128, null=True, blank=True)


class ReferenceMapper(models.Model):
    '''
    Where Payments have been made with the 'wrong' reference
    (that is one which does not exist in an `AccountDebt` model
    instance the `ReferenceMapper` object is used to map the
    reference that was used to the reference that should have been
    used
    '''

    payment_reference_used = models.CharField(max_length=128)
    payment_reference_intended = models.CharField(max_length=10)
    payment_origination_name = models.CharField(max_length=30)

    def __unicode__(self):
        return str(self.payment_reference_used) + " ( Should have been : " + str(self.payment_reference_intended) + " )"
