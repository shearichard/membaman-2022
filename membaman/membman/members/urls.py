from django.conf.urls import include, re_path
from django.contrib import admin
from django.views.generic.base import TemplateView

from . import views

'''
urlpatterns = patterns('',
    re_path(r'^$', views.IncomeListView.as_view(), name='income-list'),
)
'''
app_name = 'members'

urlpatterns = [ 
    re_path(r'^$', TemplateView.as_view(template_name='members/members-index.html'), name='membersindex'),
    re_path(r'^member-list/', views.MemberActiveListView.as_view(), name='member-list'),
    re_path(r'^member-nomore-list/', views.MemberNotActiveListView.as_view(), name='member-nomore-list'),
    re_path(r'^member-view/(?P<pk>\d+)/$', views.MemberDetail.as_view(), name='member-view'),
    re_path(r'^member-family-finance-list/', views.FamilyFinanceListView.as_view(), name='member-family-finance-list'),
    re_path(r'^member-debtors-list/', views.MemberDebtorsListView.as_view(), name='member-debtors-list'),
    re_path(r'^member-finance-list/', views.MemberFinanceListView.as_view(), name='member-finance-list'),
    re_path(r'^family-view/(?P<pk>\d+)/$', views.FamilyDetail.as_view(), name='family-view'),
]
