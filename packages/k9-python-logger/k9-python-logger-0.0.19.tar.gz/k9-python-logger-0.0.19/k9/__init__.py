import json
import logging

from dataclasses import dataclass
from k9.client import K9Core

from .models import LogMessage

BASIC_FORMAT = "%(levelname)s:%(message)s"

class K9Logger:

    app_name: str

    INFO = "INFO"
    ERROR = "ERROR"
    FATAL = "FATAL"
    DEBUG = "DEBUG"
    WARN = "WARN"

    def __init__(self, **kwargs):
        self.app_name = kwargs.get("app_name", "")
        self.k9_client = K9Core(host=kwargs.get("host"), token=kwargs.get("token"))

        if kwargs.get("logger") is None:
            logging.basicConfig(level=logging.INFO, format=BASIC_FORMAT)

    def __get_message(self, message: str, **kwargs):
        args = {
            "app_name": self.app_name,
            "log_level": kwargs.get("log_level", "INFO"),
            "correlation_id": kwargs.get("correlation_id", ""),
            "message": message,
            "span_id": kwargs.get("span_id", ""),
            "log_type": kwargs.get("log_type", "TROUBLESHOOTING")
        }
        return LogMessage(**args)

    def log(self, message, **kwargs):
        new_log: LogMessage = self.__get_message(message=message, **kwargs)
        return self.k9_client.send_request(message=json.dumps(new_log.__dict__))

    def info(self, message, **kwargs):
        logging.info(message)
        return self.log(message, log_level=self.INFO, **kwargs)

    def error(self, message, **kwargs):
        logging.error(message)
        return self.log(message, log_level=self.ERROR, **kwargs)

    def debug(self, message, **kwargs):
        logging.debug(message)
        return self.log(message, log_level=self.DEBUG, **kwargs)

    def fatal(self, message, **kwargs):
        logging.fatal(message)
        return self.log(message, log_level=self.FATAL, **kwargs)

    def warn(self, message, **kwargs):
        logging.warning(message)
        return self.log(message, log_level=self.WARN, **kwargs)