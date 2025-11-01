"""
Banking Client - Logging Setup
Copied and adapted from provided template
"""

import logging
from typing import Optional
from .config import config


def setup_logging(name: Optional[str] = None) -> logging.Logger:
    """
    Configure and return a logger instance.
    """
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format=config.LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    return logging.getLogger(name or __name__)


def get_logger(name: str) -> logging.Logger:
    """Get or create a logger with the specified name."""
    return logging.getLogger(name)


# Create module-level logger
logger = setup_logging(__name__)
