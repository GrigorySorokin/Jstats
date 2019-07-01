import logging
import datetime

from logging.handlers import RotatingFileHandler
from settings import Log as Log_conf
from tools import date_to_str


def add_time(fn):
    def wrapper(self, msg):
        _msg = f'{date_to_str(datetime.datetime.now())}::{msg}'
        return fn(self, _msg)
    return wrapper


class Log:
    """
    Выводит лог в зависимости от параметра verbosity в настройках
    """
    verbosity = -1

    def __init__(self):
        self.verbosity = Log_conf.verbosity
        handler = RotatingFileHandler(Log_conf().log_dir+Log_conf().log_file, mode='a', maxBytes=Log_conf.max_size,
                                      backupCount=2, encoding=None, delay=0)
        handler.setLevel(logging.DEBUG)
        self.log = logging.getLogger('root')
        self.log.setLevel(logging.DEBUG)
        self.log.addHandler(handler)

    @add_time
    def debug(self, msg: str):
        if self.verbosity > 1:
            self.log.debug(msg)

    @add_time
    def warn(self, msg: str):
        if self.verbosity > -1:
            self.log.warning(f'\x1b[33m{msg}\x1b[0m')

    @add_time
    def info(self, msg: str):
        if self.verbosity > 0:
            self.log.info(msg)

    @add_time
    def error(self, msg: str):
        if self.verbosity > -2:
            self.log.error(f'\x1b[31m{msg}\x1b[0m')


log = Log()
