from http.client import HTTPException


class RequestFailureException(Exception):
    """
    This is used to send error messages in response for API call
    on validation errors or handled errors
    """
    def __init__(self, error_msg='', status_code=200):
        self.error_msg = error_msg
        self.status_code = status_code

    def __str__(self):
        return self.error_msg
