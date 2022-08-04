from ..models import Year
from ..views import TEMP_ORG_ID

from django import template


register = template.Library()


@register.simple_tag
def income_year_select_content():
    '''
    This function will require more work. When used in postgres the form of
    next statement was as follows ...

    year_list = Year.objects.filter(organisation_id=TEMP_ORG_ID).distinct('start')

    ... however that's not possible to do when the db is sqlite so I've changed
    it as seen below. Depending on how the system is used (multi-home or not) this
    will matter or it won't
    '''
    year_list = Year.objects.filter(organisation_id=TEMP_ORG_ID).distinct()
    return year_list
