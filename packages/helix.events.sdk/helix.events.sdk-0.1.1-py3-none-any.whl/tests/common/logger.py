from logging import getLogger, StreamHandler, INFO, Formatter, Logger
from sys import stdout


def get_logger() -> Logger:
    logger = getLogger(__name__)
    stream_handler: StreamHandler = StreamHandler(stdout)
    stream_handler.setLevel(level=INFO)
    # noinspection SpellCheckingInspection
    formatter: Formatter = Formatter(
        '%(asctime)s.%(msecs)03d %(levelname)s %(module)s %(lineno)d - %(funcName)s: %(message)s'
    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger