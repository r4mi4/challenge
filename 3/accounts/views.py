from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import HasOrganizationAPIKey, RateLimit, ValidIp


class ExternalAPIView(APIView):
    permission_classes = [HasOrganizationAPIKey, RateLimit, ValidIp]

    def get(self, request):
        return Response({'msg': 'success'})
