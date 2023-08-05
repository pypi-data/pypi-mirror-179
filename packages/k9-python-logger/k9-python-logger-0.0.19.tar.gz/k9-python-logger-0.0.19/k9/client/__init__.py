import json
import requests

from dataclasses import dataclass
from http import HTTPStatus
from requests.utils import parse_dict_header


@dataclass
class K9CoreResponse:
    id: str
    message: str
    app_name: str
    correlation_id: str
    span_id: str
    log_level: str
    log_type: str


@dataclass
class K9CoreError():
    payload: dict
    status_code: int
    message: dict


class K9Core:

    host: str
    token: str

    def __init__(self, **kwargs):
        self.host = f"{kwargs.get('host', '')}/api/v1"
        self.token = f"{kwargs.get('token', '')}"

    def send_request(self, message):
        try:
            response = requests.post(f"{self.host}/logs",
                                     json=json.loads(message),
                                     headers=parse_dict_header(f'X-K9-Token="{self.token}"'))
            if response.ok:
                return K9CoreResponse(**response.json())
            else:
                raise Exception(message="Failed to integrate with k9 {}".format(response.status_code))
        except Exception as _:
            return K9CoreError(message=message,
                               status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                               payload=message)
