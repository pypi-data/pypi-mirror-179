import logging
from logging import StreamHandler
from django_clickhouse_logger import functions
from django.core.handlers.wsgi import WSGIRequest


class LoggerHandler(StreamHandler):

    def emit(self, record) -> None:
        if isinstance(record, logging.LogRecord) and getattr(record, "request", False) and isinstance(record.request, WSGIRequest):
            functions.logger(record)


