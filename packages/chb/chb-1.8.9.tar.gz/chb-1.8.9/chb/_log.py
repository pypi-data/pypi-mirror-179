# -*- coding: utf-8 -*-
from ._imports import *

class Log():
    """
    日志器类。
    :param logger_name: 日志器名，或者说日志文件名
    :param file_handler: 是否将日志保存到文件，为True时保存，默认为False。
    :param log_dir:保存日志的目录路径。
    :param message_only: 是否只打印消息本身（不打印时间、运行模块等其他信息），默认为False，表示打印所有信息

    from chb import *

    log = Log().getLogger('info')
    # log = Log()()  # 与上行等效

    log(123)

    输出效果如下：
    2022-11-21 21:02:41 <module> line 1 out: 123
    """
    def __init__(self, logger_name=None, file_handler=False, log_dir='.', message_only=False):
        """

        :param logger_name:
        :param file_handler:
        :param log_dir:
        """
        self.logger_name = logger_name
        if logger_name:
            self.logger = logging.getLogger(logger_name)
        else:
            self.logger = logging.getLogger('chb')
        self.logger.setLevel(level=logging.DEBUG)

        # Formatter
        file_logging_format = logging.Formatter(
            fmt='%(asctime)s , %(name)s , %(process)d, %(levelname)s , %(filename)s %(funcName)s  line %(lineno)s ,'
                ' %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S %a')


        try:  # 如果安装了colorlog就是用带颜色日志，没有安装，使用默认日志
            from colorlog import ColoredFormatter
            fmt = '%(message_log_color)s%(message)s' if message_only else '%(log_color)s%(asctime)s %(log_color)s%(funcName)s line %(log_color)s%(lineno)s out: %(message_log_color)s%(message)s'
            stream_logging_format = ColoredFormatter(
                fmt=fmt,
                datefmt='%Y-%m-%d %H:%M:%S',
                reset=True,
                log_colors={
                    'DEBUG': 'black',
                    'INFO': 'black',
                    'WARNING': 'black',
                    'ERROR': 'black',
                },
                secondary_log_colors={
                    'message': {
                        'INFO': 'green',
                        'ERROR': 'green',
                        'CRITICAL': 'green',
                        'WARNING': 'green'
                    }
                },
                style='%'
            )
        except:
            fmt = '%(message)s' if message_only else '%(asctime)s %(funcName)s line  %(lineno)s out:  %(message)s'
            stream_logging_format = logging.Formatter(
                fmt=fmt,
                datefmt='%Y-%m-%d %H:%M:%S')

        # StreamHandler
        if len(self.logger.handlers) == 0:  # 如果没有添加过日志器，则添加（避免多次创建日志器造成日志重复输出多行）
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(stream_logging_format)
            self.logger.addHandler(stream_handler)
        # FileHandler

        if file_handler:
            if len(self.logger.handlers) <= 1:  # 如果小于等于1个日志器，表明没有添加过文件日志器
                if self.logger_name:
                    log_file = os.path.join(log_dir, self.logger_name, '.log')
                else:
                    log_file = os.path.join(log_dir, 'chb.log')
                file_handler = logging.FileHandler(log_file, encoding='UTF-8')
                file_handler.setFormatter(file_logging_format)
                self.logger.addHandler(file_handler)

    def __call__(self, level='info'):
        """
        如果level为None，则返回日志器，否则返回对应等级的输出函数：debug、info等
        :param level:
        :return:
        """
        if level:
            return getattr(self.logger, level)
        else:
            return self.logger

    def getLogger(self, level='info'):
        """
        如果level为None，则返回日志器，否则返回对应等级的输出函数：debug、info等
        :param level:
        :return:
        """
        return self.__call__(level)

