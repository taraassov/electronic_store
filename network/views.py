from rest_framework import generics
from network.models import Network
from network.serializers import NetworkSerializer


class NetworksCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkSerializer


class NetworksListAPIView(generics.ListAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()


class NetworksRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()


class NetworksUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()


class NetworksDestroyAPIView(generics.DestroyAPIView):
    queryset = Network.objects.all()