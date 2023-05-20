from django.urls import path
from .views import AdsList, AdDetail, AdCreate, ResponseList, ResponseCreate, AdUpdate, AdDelete

urlpatterns = [
    path('', AdsList.as_view(), name='ads_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/update/', AdUpdate.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
    path('responses/', ResponseList.as_view(), name='responses'),
    path('<int:ad>/responses/create/', ResponseCreate.as_view(), name='responses_create'),
]
