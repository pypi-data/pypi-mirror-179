import logging
from typing import Optional

import structlog
from structlog import contextvars
from structlog.typing import EventDict

from payla_utils.logging.default_configuration import get_default_logging_conf


class LoggerSetupError(Exception):
    pass


class LoggingConfigurator:
    def __init__(
        self,
        service_name: str,
        log_level: str,
        own_apps: Optional[list] = None,
        config: Optional[dict] = None,
        setup_logging_dict: bool = False,
    ):
        self.service_name = service_name
        self.log_level = log_level.upper()
        self.config = config
        self.own_apps = own_apps or []
        self.setup_logging_dict = setup_logging_dict

    @staticmethod
    def add_logger_name(logger: logging.Logger, method_name: str, event_dict: EventDict) -> EventDict:
        """
        Add the logger name to the event dict.
        """
        record = event_dict.get("_record")
        if record is None:
            event_dict["logger"] = logger.name
        else:
            event_dict["logger"] = record.name
        return event_dict

    def get_processors(self) -> list:
        processors = [
            contextvars.merge_contextvars,
            self.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.filter_by_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.dev.set_exc_info,
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.ExceptionPrettyPrinter(),
            structlog.stdlib.ExtraAdder(),
            structlog.processors.EventRenamer(to="message"),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ]
        return processors

    def configure_structlog(self, custom_processors=None, formatter='json_formatter'):

        if self.setup_logging_dict:
            logger_init_config = self.config
            if not self.config:
                logger_init_config = get_default_logging_conf(
                    log_level=self.log_level,
                    own_apps=self.own_apps,
                    formatter=formatter,
                )

            logging.config.dictConfig(logger_init_config)

        processors = custom_processors or self.get_processors()

        structlog.configure(
            processors=processors,
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )
