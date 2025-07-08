import structlog
import logging

logging.basicConfig(level=logging.INFO)
logger = structlog.get_logger()

def log_event(event: str, **kwargs):
    logger.info(event, **kwargs)
