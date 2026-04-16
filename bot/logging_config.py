import os
import logging
import sys
from dotenv import load_dotenv

class ConsoleFormatter(logging.Formatter):
    """Formatter that strips exception tracebacks for cleaner console output."""
    def format(self, record):
        original_exc_info = record.exc_info
        original_exc_text = record.exc_text
        record.exc_info = None
        record.exc_text = None
        try:
            return super().format(record)
        finally:
            record.exc_info = original_exc_info
            record.exc_text = original_exc_text

def setup_logger(name: str = "trading_bot", log_file: str = None) -> logging.Logger:
    """
    Configures and returns a logger instance that writes to both console and a file.
    Reads LOG_LEVEL and LOG_FILE from environment variables for safe modular config.
    Prevents duplicate handlers if called multiple times.
    """
    # Pre-emptively load env variables so it can govern logger configuration
    load_dotenv()
    
    logger = logging.getLogger(name)

    # Check if handlers are already configured to prevent duplicate logs
    if not logger.handlers:
        
        # Pull level from Envs, default predictably to INFO
        log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
        log_level = getattr(logging, log_level_str, logging.INFO)
        
        # Override file target via environment conditionally
        if log_file is None:
            log_file = os.getenv("LOG_FILE", "trading_bot.log")

        logger.setLevel(log_level)
            
        # Format natively: timestamp | level | module | message
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(module)s | %(message)s')
        console_formatter = ConsoleFormatter('%(asctime)s | %(levelname)s | %(module)s | %(message)s')

        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_handler.setFormatter(console_formatter)

        # File Handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
