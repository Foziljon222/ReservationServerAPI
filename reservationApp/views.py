from rest_framework import generics, permissions
from .models import Restourant, Table, Reservation
from .serializers import ReservationSerializer, TableSerializer, RestaurantSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User


class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restourant.objects.all()
    serializer_class = RestaurantSerializer


class TableListCreateView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReservationCancelView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CusterAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request,*args, **kwargs)
        token = Token.objects.get(user=self.user)
        return Response({'token': token.key})
