from rest_framework.exceptions import APIException


class APIError(APIException):
    # Error properties
    error_code: int
    error_name: str
    error_message: str

    string_args = []


class SerializerHasNoField(APIError):
    status_code = 400
    error_code = 3
    error_name = 'serializer_no_field'
    error_message = 'No field: {0} in serializer: {1}'

    def __init__(self, bind_value: []):
        super()
        self.error_message = self.error_message.format(*bind_value)
        self.detail = self.error_message


class MethodNotAllowed(APIError):
    status_code = 405
    error_code = 2
    error_name = 'method_not_allowed'
    error_message = 'Method: {0} not allowed on node: {1}'
