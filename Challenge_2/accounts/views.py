from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTokenValid
from .models import BlackToken, Profile


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsTokenValid, IsAuthenticated)
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        access_token = request.auth
        BlackToken.objects.get_or_create(user_id=access_token['user_id'], token=access_token)
        tokens = OutstandingToken.objects.filter(user_id=access_token['user_id'])
        for token in tokens:
            BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
