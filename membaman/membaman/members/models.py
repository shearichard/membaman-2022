from django.db import models

class Organisation(models.Model):
    '''
    An `Organisation` is an entity to which
    `Member` belong
    '''
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=50)
    postal_address = models.CharField(max_length=150, null=True, blank=True)
    bank_account_name = models.CharField(max_length=100, null=True, blank=True)
    bank_account_number = models.CharField(max_length=50, null=True, blank=True)
    treasurer_name = models.CharField(max_length=50, null=True, blank=True)
    treasurer_phone = models.CharField(max_length=50, null=True, blank=True)
    treasurer_email = models.CharField(max_length=50, null=True, blank=True)
    leader_name = models.CharField(max_length=50, null=True, blank=True)
    leader_phone = models.CharField(max_length=50, null=True, blank=True)
    leader_email = models.CharField(max_length=50, null=True, blank=True)


    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return self.name 


class SubOrganisation(models.Model):
    '''
    A `SubOrganisation` is grouping within an
    `Organisation` to which a `Member` primarily
    identifies
    '''
    class Meta:
        ordering = ['sub_name']

    sub_name = models.CharField(max_length=50)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)

    def organisation_name(self):
        return self.organisation.name
    organisation_name.short_description = 'Organisation Name'

    def __unicode__(self):
        return str(self.sub_name) + str(' (') + str(self.organisation.name) + str(')')

    def __str__(self):
        return self.sub_name 

class Family(models.Model):
    '''
    `Family` constitutes one or more `Caregiver` and one or
    more `Member`
    '''
    class Meta:
        ordering = ['street_address', 'suburb', 'city']

    street_address = models.CharField(max_length=75)
    suburb = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    phone_fixed = models.CharField(max_length=20)

    def __unicode__(self):
        return u', '.join((str(self.street_address), str(self.suburb), str(self.city)))

    def __str__(self):
        return self.street_address 

class Person(models.Model):
    '''
    `Person` is an abstract Model to accomodate personal
    identity
    '''
    class Meta:
        abstract = True

    name_given = models.CharField('given name', max_length=50)
    name_family = models.CharField('family name', max_length=50)

    def __str__(self):
        return f'''{self.name_family} , {self.name_given}'''


class Caregiver(Person):
    '''
    `Caregiver` is someone who cares for a `Member`
    '''
    class Meta:
        ordering = ['name_family', 'name_given']

    MOTHER = 'MO'
    FATHER = 'FA'
    GRANDMOTHER = 'GM'
    GRANDFATHER = 'GF'
    SIBLING = 'SI'
    OTHER = 'OT'
    RELATIONSHIP_TYPE_CHOICES = (
        (MOTHER, 'Mother'),
        (FATHER, 'Father'),
        (GRANDMOTHER, 'Grandmother'),
        (GRANDFATHER, 'Grandfather'),
        (SIBLING, 'Sibling'),
        (OTHER, 'Other'),
    )

    family = models.ForeignKey(Family, on_delete=models.PROTECT)
    phone_mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    relationship = models.CharField(max_length=2,
                                    choices=RELATIONSHIP_TYPE_CHOICES,
                                    default=OTHER)

    def __unicode__(self):
        return u', '.join((str(self.name_family), str(self.name_given)))

class Member(Person):
    '''
    `Member` is a `Person` who directly participates in an `Organisation`
    '''
    class Meta:
        ordering = ['name_family', 'name_given']

    KEA = 'KE'
    CUB = 'CU'
    SCOUT = 'SC'
    VENTURER = 'VE'
    UNKNOWN = 'UK'
    MEMBERSHIP_TYPE_CHOICES = (
        (KEA, 'Kea'),
        (CUB, 'Cub'),
        (SCOUT, 'Scout'),
        (VENTURER, 'Venturer'),
        (UNKNOWN, 'Unknown'),
    )
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    sub_organisation = models.ForeignKey(SubOrganisation, on_delete=models.PROTECT)
    membership_type = models.CharField(max_length=2,
                                       choices=MEMBERSHIP_TYPE_CHOICES,
                                       default=UNKNOWN)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)
    primary_caregiver = models.ForeignKey(Caregiver, on_delete=models.PROTECT, related_name='primary_caregiver')
    caregivers = models.ManyToManyField(Caregiver, related_name='caregivers')
    date_of_birth = models.DateField(null=True, blank=True)
    date_invested = models.DateField(null=True, blank=True)
    no_longer_attends = models.BooleanField(default=False)
    no_longer_attends_notification = models.DateField(null=True, blank=True)

    def __unicode__(self):
        '''
        Returns "Smith, John"
        '''
        return u', '.join((str(self.name_family), str(self.name_given)))

    def last_first_name(self):
        '''
        Returns "Smith, John"
        '''
        return u', '.join((str(self.name_family), str(self.name_given)))

    def first_last_name(self):
        '''
        Returns "John Smith"
        '''
        return u' '.join((str(self.name_given), str(self.name_family)))

    def first_last_name_memtype_desc(self):
        '''
        Returns "John Smith (Scout)"
        '''
        out = self.first_last_name()
        if self.membership_type == self.UNKNOWN:
            pass
        else:
            for mem_type_tuple in self.MEMBERSHIP_TYPE_CHOICES:
                if mem_type_tuple[0] == self.membership_type:
                    outfull = u"%s (%s)" % (out, str(mem_type_tuple[1]))
                    out = outfull
                    break
        return out

    def primary_caregiver_email(self):
        return str(self.primary_caregiver.email)

