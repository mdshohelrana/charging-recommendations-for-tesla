from typing import Any
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from solar.services.solar_production_service import SolarProductionService

class GetChargingPricesDataView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.solar_production_service = SolarProductionService()

    def get(self, request):
        data = self.solar_production_service.get_charging_prices_data()
        return Response(data,status=status.HTTP_200_OK)