from django.urls import path
from network.apps import NetworkConfig
from network.views import NetworksListAPIView, NetworksCreateAPIView, NetworksRetrieveAPIView, NetworksUpdateAPIView, \
    NetworksDestroyAPIView

app_name = NetworkConfig.name


urlpatterns = [
    path('', NetworksListAPIView.as_view(), name='network_list'),
    path('create/', NetworksCreateAPIView.as_view(), name='network-create'),
    path('retrieve/<int:pk>/', NetworksRetrieveAPIView.as_view(), name='network-retrieve'),
    path('update/<int:pk>/', NetworksUpdateAPIView.as_view(), name='network-update'),
    path('delete/<int:pk>/', NetworksDestroyAPIView.as_view(), name='network-delete'),
]