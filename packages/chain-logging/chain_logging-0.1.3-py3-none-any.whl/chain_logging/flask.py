import logging
import time
import sys
import typing
from flask import Flask, current_app, g, request, Response
from functools import wraps
from werkzeug.local import LocalProxy
from werkzeug.exceptions import HTTPException


class ChainFilter(logging.Filter):
    """
    Chain Filter for chained logging tools

    Params:
        - log_format (str) : use `exec_id` on your format to enable unique id for each request
        - level (int) : log level (NOTSET < DEBUG < INFO < ERROR < WARNING < CRITICAL)
        - **kargs (Mapped[Any, Any]) : put your desired value to the filter
            ex:
                - logformat = [%(asctime)s][%(my_name)s][%(my_age)s] - %(message)s'
                - here `my_name` and `my_age` is a custom value to `LogRecord` object
                - applying this format to the logger would enable you to insert the value :
                    `ChainFilter(log_format, logging.INFO, my_name="joy", my_age=22)`
    """
    def __init__(
        self,
        log_format: str = '[%(asctime)s][ID:%(exec_id)s][%(filename)s:%(lineno)s][%(levelname)s] - %(message)s',
        level: int = logging.INFO,
        id_generator: typing.Optional[typing.Callable] = None,
        **kargs
    ):
        self.disabled = False
        self.level = level
        self._unapplied = ["_log_format", "_unapplied"]
        self._log_format = log_format
        self._kargs = kargs
        self._embed_attr(**kargs)
        if not callable(id_generator):
            id_generator = time.time_ns
        self._exec_id = id_generator()

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, val):
        self.__level = logging._checkLevel(val)

    @property
    def allowed_levels(self):
        """
        Allowed filter levels property

        Return:
            - levels (List[int]) : allowed levels to be logged
        """
        raw_levels = list(logging._nameToLevel.values())
        if self.level:
            levels = [lv for lv in raw_levels if lv >= self.level]
        else:
            levels = []
        return levels

    def _embed_attr(self, **kargs):
        """
        Embed the mapped key-value into to self `ChainFilter` object
        """
        if kargs:
            for key in kargs:
                if not key in self.__dict__:
                    setattr(self, key, kargs[key])

    def _apply_record_attr(self, record: logging.LogRecord):
        """
        Apply attribute from `ChainFilter` object to the log record

        Params:
            - record (logging.LogRecord)
        """
        for attr, value in vars(self).items():
            if (attr not in record.__dict__) and (attr not in self._unapplied):
                setattr(record, attr, value)
        setattr(record, "exec_id", self._exec_id)

    def filter(self, record: logging.LogRecord):
        if not self.disabled and record.levelno in self.allowed_levels:
            self._apply_record_attr(record)
            return True
        return False

    def get_child_filter(self):
        """
        Generate child filter

        Return:
            - new_chain_filter (ChainFilter)

        """
        new_chain_filter = ChainFilter(self._log_format, self.level, **self._kargs)
        return new_chain_filter


class ChainStreamer(logging.StreamHandler):
    """
    Stream Handler for `ChainLogger`

    Params:
        - filter_object (ChainFilter)
    """
    def __init__(self, filter_object: ChainFilter):
        super(ChainStreamer, self).__init__(sys.stdout)
        self._formatter = logging.Formatter(filter_object._log_format)
        self.setFormatter(self._formatter)
        self.addFilter(filter_object)
        self._filter = filter_object
        self.setLevel(self._filter.level)


class ChainLogger(logging.getLoggerClass()):
    """
    Chained Logger

    This logger is used to chain every logger used in every request in every function
    to be used the same logger with the same request id

    Params:
        - name (str)
        - filter_object (ChainFilter)
    """
    def __init__(self, name: str, filter_object: ChainFilter):
        super(ChainLogger, self).__init__(name, 0)
        self._streamer = ChainStreamer(filter_object)
        self.addHandler(self._streamer)
        self._filter = filter_object
        self.setLevel(self._filter.level)

    @property
    def _exec_id(self):
        """`_exec_id` properties. represent the request id"""
        return self._filter._exec_id

    @_exec_id.setter
    def _exec_id(self, exec_id):
        """`_exec_id` setter"""
        self._filter._exec_id = exec_id

    def disable(self):
        """disable the logger"""
        self._filter.disabled = True

    def enable(self):
        """enable the logger"""
        self._filter.disabled = False

    @property
    def time_elapsed(self):
        """
        Elapsed time in miliseconds. Measured since the logger is initiated before
        request is dispached until this properties is called.

        Every time this property is called, it will also update the elapsed time

        Return:
            - elapsed (int) : time in miliseconds with 2 decimal
        """
        elapsed = time.time_ns()-self._exec_id
        elapsed = round(elapsed/1e6, 2)
        return elapsed

    def get_child_logger(self):
        """
        Generate child logger
        """
        child_filter = self._filter.get_child_filter()
        return ChainLogger(self.name, child_filter)


_base_logger = None


def chain_with_parent_logger(func):
    """
    [CELERY USE ONLY]

    Chain the worker logger with the parent logger.
    Actually just bind the execution id for easier tracking

    Please add `_exec_id` keyword-arguments on your call in `<function_name>.delay(_exec_id=logger._exec_id)` to enable

    Params:
        - func (callable) : unchained celery task

    Returns:
        - wrapped_func (callable) : chained celery task
    """
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        """
        Wraps the chained celery task

        Params:
            - _exec_id (int) : parent execution id
        Returns:
            - func (callable) : chained celery task
        """
        global _base_logger

        if not "_exec_id" in kwargs:
            raise TypeError("Please add `_exec_id` keyword-arguments on your call in `<function_name>.delay(_exec_id=logger._exec_id)` to enable")

        g._logger = _base_logger
        g._logger._exec_id = kwargs.pop("_exec_id")

        return func(*args, **kwargs)

    return wrapped_func


def setup_chained_logger(
    app: Flask,
    logger: typing.Optional[ChainLogger] = None,
    before_request: typing.Optional[typing.Callable] = None,
    after_request: typing.Optional[typing.Callable] = None,
    handle_exception: bool = False
):
    """
    Setup the middleware of chained logger that has a unique request ID
    this is used to distinct each request log for each other
    so we could distinct every process

    Please setup any logger modification after setup this log
    because anything you write under root logger will be cleaned

    This setup allows you to use chained logger either from `current_app.logger` or `log_tools.logger`
    It doesn't matter what function you're running, as long as you call the logger from between
    those 2, you are actually using the same logging handler

    Params:
        - app (Flask)
        - handle_exception (bool)
    """
    global _base_logger

    if not logger:
        logger = ChainLogger(name="FlaskChainLogger", filter_object=ChainFilter())

    assert isinstance(logger, ChainLogger)
    _base_logger = logger

    # override handlers to avoid multiple channels print out the same output
    root_logger = logging.getLogger()
    root_logger.setLevel(_base_logger._filter.level)
    app.logger.handlers = _base_logger.handlers

    # applying middleware
    app.before_request(init_global_logger)

    if callable(before_request):
        app.before_request(before_request)
    else:
        def before_request_call():
            g._logger.info(f"Received {request.method} {request.path}")
        app.before_request(before_request_call)

    if callable(after_request):
        app.after_request(after_request)
    else:
        def after_request_call(response: Response):
            current_app.logger.info(f"Request done in {logger.time_elapsed}ms")
            return response
        app.after_request(after_request_call)

    if handle_exception:
        app.errorhandler(Exception)(traceback_error_logger)


def init_global_logger():
    """
    Enabling the logger `LocalProxy` to be used globally.
    Its an initiation of logger with different id that distinct each request for easier tracking
        and avoid any messy logging due to massive request

    g._logger -> will enable the `logger` to be used whenever its imported using flask's `LocalProxy`
    get_child_logger -> will return a logger with different execution id (exec_id),
        this exec_id is equals with request id where each request will only have one
        this could easily tracks the request in a server with massive request without any worries
        to get lost in track because we have the exec_id

    Child logger is used to make each request has different execution id.
    """
    global _base_logger
    g._logger = _base_logger.get_child_logger()
    current_app.logger.handlers[0] = g._logger.handlers[0]


def traceback_error_logger(error: Exception):
    """
    Log any errors before raised to `Traceback`

    Params:
        - error (Exception)

    Raises:
        - InvalidUsage: won't be logged
        - Exception: errors will be raised if catched,
            means error is not handled in code level
    """
    if isinstance(error, HTTPException):
        logger.error(f"[HTTPException] : {error}")
        return error

    logger.error(f"[TRACEBACK] : {error}")
    raise error


def get_global_logger():
    """
    Get global logger in `LocalProxy` scope

    Returns:
        - logger (ChainLogger)
    """
    global _base_logger
    if not "_logger" in vars(g):
        g._logger = _base_logger
    return g._logger


logger: ChainLogger = LocalProxy(get_global_logger)
