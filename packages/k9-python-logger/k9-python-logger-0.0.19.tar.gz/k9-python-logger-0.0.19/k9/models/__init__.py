from dataclasses import dataclass


@dataclass
class LogMessage:
    app_name: str
    correlation_id: str
    log_level: int
    message: str
    span_id: str
    log_type: str

    def __str__(self):
        msg = {
            "app_name": self.app_name,
            "log_level": self.log_level,
            "correlation_id": self.correlation_id,
            "message": self.message,
            "span_id": self.span_id,
            "log_type": self.log_type
        }
        return f'{msg}'