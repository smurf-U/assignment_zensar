from django.urls import path, include
from django.conf.urls import url

from .views import RouterManagerList, RouterManagerDelete, RouterManagerUpdate, RouterManagerDetail, RouterManagerCreate, search_router, router_list, router_detail, delete_router_based_on_ip, api_list

from rest_framework import routers 
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter() 
# router.register(r'router', RouterManagerView, 'rest-view')
# router.register(r'router', delete_router_based_on_ip, 'delete_router_based_on_ip')

urlpatterns = [
    path('search_router/', search_router, name='search_router'),
    path('', RouterManagerList.as_view(), name='routermanager_list'),
    path('detail/<int:pk>', RouterManagerDetail.as_view(), name='routermanager_detail'),
    path('create', RouterManagerCreate.as_view(), name='routermanager_create'),
    path('update/<int:pk>', RouterManagerUpdate.as_view(), name='routermanager_update'),
    path('delete/<int:pk>', RouterManagerDelete.as_view(), name='routermanager_delete'),
]

rest_urlpatterns = [
    path('api/', api_list),
    path('api/router/', router_list),
    path('api/router/<int:pk>', router_detail),
    path('api/router/delete_base_on_ip', delete_router_based_on_ip , name='delete_router_based_on_ip'),
]

urlpatterns += format_suffix_patterns(rest_urlpatterns)
