from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

from boss_test.apps.authentification.serializers import RegisterSerializer, EmailTokenObtainPairSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """
    Принимает юзернейм, эл. почту и пароль, возвращает юзернейм, эл. почту.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = RegisterSerializer
