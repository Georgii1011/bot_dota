# utils/errors.py

import logging

def log_exception(e: Exception, context: str = ""):
    logging.exception(f"❗ Ошибка в {context}: {e}")
