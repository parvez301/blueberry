from typing import Optional, Dict
from http import HTTPStatus
from django.http import JsonResponse

from parking_lot.exceptions import RequestFailureException


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """

    def __init__(self):
        super().__init__()

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except RequestFailureException as err:
            return self.render_to_json_response(error=err.error_msg, status=HTTPStatus.BAD_REQUEST)
        except Exception as err:
            return self.render_to_json_response(error=str(err),
                                                status=HTTPStatus.INTERNAL_SERVER_ERROR)

    def render_to_json_response(self, data: Optional[Dict] = {}, meta: Optional[Dict] = {},
                                error: Optional[str] = '', status=HTTPStatus.OK, **response_kwargs):
        """
        Returns a JSON response, transforming 'data' to make the payload.
        """
        response_data = {"body": data, "meta": meta, "error": error}
        return JsonResponse(response_data, status=status, **response_kwargs)
