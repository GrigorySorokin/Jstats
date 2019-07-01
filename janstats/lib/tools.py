from datetime import datetime
import time
from django.utils import timezone

from app_gss.lib.settings import Bapi_connector_conf
#from app_gss.lib.log import log
def record_time(fn):

    """
        Декаратор для изменении времени выполнения
    :param fn: Функция время выполнение, которой надо померить
    :return:
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        print(f'___________{fn.__name__}______________')
        print(f'{time.time() - start_time} sec')
        return res
    return wrapper


def str_to_date(chars: 'YYYY-MM-DD HH:mm:ss'):
    """
        Перевод строки datetime с форматом YYYY-MM-DD HH:mm:ss
    :param chars: строка вида YYYY-MM-DD HH:mm:ss
    :return: datetime
    """
    # ugly optimization
    return datetime(
        int(chars[0:4]),  # %Y
        int(chars[5:7]),  # %m
        int(chars[8:10]),  # %d
        int(chars[11:13]),  # %H
        int(chars[14:16]),  # %M
        int(chars[17:19]),  # %s
    )
    # return datetime.strptime(chars, '%Y-%m-%d %H:%M:%S')


def date_to_str(date):
    """
        Перевод datetime в строку
    :param date: datetime строка вида YYYY-MM-DD HH:mm:ss
    :return: строка вида YYYY-MM-DD HH:mm:ss
    """
    return date.strftime('%Y-%m-%d %H:%M:%S')


def get_param(CTS, interval, q_type):
    
    
    result = ""
    if q_type == 'T':
        result = {"data": {"arg-rat": ["2G", "3G", "4G"],
                  "arg-ttype":["dns","icq-msg","sip","http","ftp-cmd","mail-msg","pop3-login","icq-login","raw"],
                  "arg-date": [[int(time.mktime(CTS.timetuple())),
                                int(time.mktime(interval.timetuple()))]],
                  "type": Bapi_connector_conf.type[q_type]}}
    if q_type == 'W':
        result = {"data": {"arg-rat": ["2G", "3G", "4G"],
                  "arg-date": [[int(time.mktime(CTS.timetuple())),
                                int(time.mktime(interval.timetuple()))]],
                  "type": Bapi_connector_conf.type[q_type]}}
    if q_type == 'S':
        result = {"data": {"arg-rat": ["2G", "3G", "4G"],
                  "arg-date": [[int(time.mktime(CTS.timetuple())),
                                int(time.mktime(interval.timetuple()))]],
                  "arg-returns": ["raw-sessions"],
                  "type": Bapi_connector_conf.type[q_type]}}
    if q_type == 'BT':
        result = {"data": {
                  "arg-ttype":["dns","icq-msg","sip","http","ftp-cmd","mail-msg","pop3-login","icq-login","raw"],
                  "arg-raw-protocol":[],
                  "arg-date": [[int(time.mktime(CTS.timetuple())),
                                int(time.mktime(interval.timetuple()))]],
                  "type": Bapi_connector_conf.type[q_type]}}
    if q_type == 'BS':
        result = {"data": {
                  "arg-date": [[date_to_str(timezone.localtime(CTS)),
                                date_to_str(timezone.localtime(CTS) + interval)]],
                  "type": Bapi_connector_conf.type[q_type]}}

  
    return result