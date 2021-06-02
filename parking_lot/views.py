import json
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import HttpRequest, JsonResponse

from parking_lot.mixins import JSONResponseMixin
from parking_lot import utils as parking_lot_utils
from parking_lot.lib import ChoiceIntEnum


class ParkingLot(JSONResponseMixin, View):
    """
    View to handle parking lot data
    """

    # Protect this view so only logged in user can access that
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # TODO: Add authorization so only authorized users can add new parking lots
    def post(self, request: HttpRequest) -> JsonResponse:
        """
        API to create the parking lot
        """
        request_data = json.loads(request.body.decode(encoding='UTF-8'))
        try:
            response_body = parking_lot_utils.create_new_parking_lot(request_data)
        except Exception as err:
            return self.render_to_json_response(data=f'[Exception Occured]: {str(err)}', status=400)

        return self.render_to_json_response(data=response_body)


class ParkingLotRateCard(JSONResponseMixin, View):
    """
    View to handle parking lot rate card
    """

    # Protect this view so only logged in user can access that
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # TODO: Add authorization so only authorized users can add new parking lots
    def post(self, request: HttpRequest) -> JsonResponse:
        """
        API to create the parking lot
        """
        request_data = json.loads(request.body.decode(encoding='UTF-8'))
        try:
            response_body = parking_lot_utils.create_parking_lot_rate_card(request_data)
        except Exception as err:
            return self.render_to_json_response(data=f'[Exception Occured]: {str(err)}', status=400)

        return self.render_to_json_response(data=response_body)


class VehicleHistory(JSONResponseMixin, View):
    """
    View to handle parking lot data
    """

    # Protect this view so only logged in user can access that
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # TODO: Add authorization so only authorized users can add new parking lots
    def get(self, request: HttpRequest) -> JsonResponse:
        """
        API to create the parking lot
        """
        request_data = json.loads(request.body.decode(encoding='UTF-8'))
        try:
            response_body = parking_lot_utils.get_parked_vehicle_history(request_data)
        except Exception as err:
            return self.render_to_json_response(data=f'[Exception Occured]: {str(err)}', status=400)

        return self.render_to_json_response(data=response_body)


class ParkVehicle(JSONResponseMixin, View):
    """
    View to handle parking lot data
    """

    # Protect this view so only logged in user can access that
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # TODO: Add authorization so only authorized users can add new parking lots
    def post(self, request: HttpRequest) -> JsonResponse:
        """
        API to create the parking lot
        """
        request_data = json.loads(request.body.decode(encoding='UTF-8'))
        try:
            response_body = parking_lot_utils.park_vehicle(request_data)
        except Exception as err:
            return self.render_to_json_response(data=f'[Exception Occured]: {str(err)}', status=400)

        return self.render_to_json_response(data=response_body)
