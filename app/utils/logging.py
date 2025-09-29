import logging
import sys

def setup_logging():
    handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter(fmt="%(asctime)s %(levelname)s %(name)s :: %(message)s")
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler.setFormatter(fmt)
    root.handlers.clear()
    root.addHandler(handler)
