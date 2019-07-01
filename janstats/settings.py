import platform


class Log:
    """
    Настройки лога
    max_size - Максимальный размер файла в байтах
    verbosity - уровень детализоции лога
    log_file - название файла
    log_dir - путь до файла
    """

    max_size = 5 * 1024 * 1024
    verbosity = 1
    log_file = 'janstats.log'
    log_dir = ''

    def __init__(self):
        if platform.system() == 'Windows':
            self.log_dir = 'E:\\log\\'
        else:
            self.log_dir = '/home/gsorokin/log/'

