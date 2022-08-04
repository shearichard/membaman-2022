from django.conf.urls import re_path
from django.views.generic.base import TemplateView

from . import views

app_name = 'fees'

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='fees/fees-index.html'), name='feesindex'),
    re_path(r'^income-list/', views.IncomeListView.as_view(), name='income-list'),
    re_path(r'^income-list-subyear/', views.IncomeListSubYearView.as_view(), name='income-list-subyear'),
]
