from django.conf.urls import url
from . import views

app_name = 'care_point'

urlpatterns = [

    #index /competition
    url(r'^$', views.index, name='index'),

    #OPIEKINOWIE
    url(r'^caregiver/$', views.caregiver, name='caregiver'),
    url(r'^caregiver/add/$', views.caregiver_add, name='caregiver_add'),
    url(r'^caregiver/(?P<caregiver_id>[0-9]+)/$', views.caregiver_details, name='caregiver_details'),
    url(r'^caregiver/(?P<caregiver_id>[0-9]+)/delete/$', views.caregiver_delete, name='caregiver_delete'),
    url(r'^caregiver/(?P<caregiver_id>[0-9]+)/update/$', views.caregiver_update, name='caregiver_update'),

    #CONTRACT
    url(r'^contract/$', views.contract, name='contract'),
    url(r'^contract/add/$', views.contract_add, name='contract_add'),
    url(r'^contract/caregiver/$', views.contract_add_caregiver, name='contract_add_caregiver'),
    url(r'^contract/caregiver/(?P<caregiver_id>[0-9]+)/next$', views.next_contract, name='next_contract'),
    url(r'^contract/caregiver/(?P<caregiver_id>[0-9]+)/$', views.new_worksheet_caregiver, name='new_worksheet_caregiver'),

    url(r'^contract/(?P<contract_id>[0-9]+)/$', views.contract_details, name='contract_details'),
    url(r'^contract/(?P<contract_id>[0-9]+)/delete/$', views.contract_delete, name='contract_delete'),
    url(r'^contract/(?P<contract_id>[0-9]+)/update/$', views.contract_update, name='contract_update'),

    #WARD
    url(r'^ward/$', views.ward, name='ward'),
    url(r'^ward/add/$', views.ward_add, name='ward_add'),
    url(r'^contract/ward/(?P<ward_id>[0-9]+)/$', views.new_worksheet_ward, name='new_worksheet_ward'),
    url(r'^ward/(?P<ward_id>[0-9]+)/$', views.ward_details, name='ward_details'),
    url(r'^ward/(?P<ward_id>[0-9]+)/delete/$', views.ward_delete, name='ward_delete'),
    url(r'^ward/(?P<ward_id>[0-9]+)/update/$', views.ward_update, name='ward_update'),
    #
    # #DECYZJE
    url(r'^decision/$', views.decision, name='decision'),
    url(r'^decision/add/$', views.decision_add, name='decision_add'),
    url(r'^decision/(?P<ward_id>[0-9]+)/$', views.next_decision, name='next_decision'),
    url(r'^decision/(?P<decision_id>[0-9]+)/$', views.decision_details, name='decision_details'),
    url(r'^decision/(?P<decision_id>[0-9]+)/delete/$', views.decision_delete, name='decision_delete'),
    url(r'^decision/(?P<decision_id>[0-9]+)/update/$', views.decision_update, name='decision_update'),
    #
    # #ILLNESS
    url(r'^illness/$', views.illness, name='illness'),
    url(r'^illness/add/$', views.illness_add, name='illness_add'),
    url(r'^illness/(?P<illness_id>[0-9]+)/$', views.illness_details, name='illness_details'),
    url(r'^illness/(?P<illness_id>[0-9]+)/delete/$', views.illness_delete, name='illness_delete'),
    url(r'^illness/(?P<illness_id>[0-9]+)/update/$', views.illness_update, name='illness_update'),
    #
    # #ACTIVITY
    url(r'^activity/$', views.activity, name='activity'),
    url(r'^activity/add/$', views.activity_add, name='activity_add'),
    url(r'^activity/(?P<activity_id>[0-9]+)/$', views.activity_details, name='activity_details'),
    url(r'^activity/(?P<activity_id>[0-9]+)/delete/$', views.activity_delete, name='activity_delete'),
    url(r'^activity/(?P<activity_id>[0-9]+)/update/$', views.activity_update, name='activity_update'),
    #
    # #MANAGER
    # url(r'^manager/$', views.manager, name='manager'),
    # url(r'^manager/add/$', views.manager_add, name='manager_add'),
    # url(r'^manager/(?P<manager_id>[0-9]+)/$', views.manager_details, name='manager_details'),
    # url(r'^manager/(?P<manager_id>[0-9]+)/delete/$', views.manager_delete, name='manager_delete'),
    # url(r'^manager/(?P<manager_id>[0-9]+)/update/$', views.manager_update, name='manager_update'),
    #
    # #ADDRESS
    url(r'^address/$', views.address, name='address'),
    url(r'^address/add/$', views.address_add, name='address_add'),
    url(r'^address/(?P<address_id>[0-9]+)/$', views.address_details, name='address_details'),
    url(r'^address/(?P<address_id>[0-9]+)/delete/$', views.address_delete, name='address_delete'),
    url(r'^address/(?P<address_id>[0-9]+)/update/$', views.address_update, name='address_update'),
    #
    # WORKSHEET
    url(r'^worksheet/$', views.worksheet, name='worksheet'),
    url(r'^worksheet/add/$', views.worksheet_add, name='worksheet_add'),
    url(r'^worksheet/(?P<worksheet_id>[0-9]+)/$', views.worksheet_details, name='worksheet_details'),
    url(r'^worksheet/(?P<worksheet_id>[0-9]+)/delete/$', views.worksheet_delete, name='worksheet_delete'),
    url(r'^worksheet/(?P<worksheet_id>[0-9]+)/update/$', views.worksheet_update, name='worksheet_update'),
]


