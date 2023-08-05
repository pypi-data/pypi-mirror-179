import inspect
import logging
import sys
import time
import typing
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class ChainFilter(logging.Filter):
    """
    Chain Filter for chained logging tools

    Params:
        - log_format (str) : can use `exec_id` as our attributes to handle request id
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
        log_format: str = "[%(asctime)s][ID:%(exec_id)s][%(filename)s:%(lineno)s][%(levelname)s] - %(message)s",
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
        if not id_generator:
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

    async def get_child_filter(self):
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

    async def get_child_logger(self):
        """
        Generate child logger
        """
        child_filter = await self._filter.get_child_filter()
        return ChainLogger(self.name, child_filter)


async def get_chained_logger(request: Request) -> ChainLogger:
    if "_logger" not in vars(request.state).get("_state"):
        await ChainLoggerMiddleware.initiate_logger(request)
    return request.state._logger


class ChainLoggerMiddleware(BaseHTTPMiddleware):
    """
    Enable logging with unique ID for each request

    :params: before_request
    ```
    async def before_request_call(request: Request):
        # do something
        ...
    ```

    :params: after_request
    ```
    async def after_request_call(request: Request, response: Response):
        # do something
        ...
    ```
    """
    _base_logger = None

    def __init__(
        self, app: FastAPI,
        logger: typing.Optional[ChainLogger] = None,
        before_request: typing.Union[bool, typing.Callable, None] = False,
        after_request: typing.Union[bool, typing.Callable, None] = False,
    ):
        super().__init__(app)

        if not logger:
            logger = ChainLogger(name="FastAPIChainLogger", filter_object=ChainFilter())

        assert isinstance(logger, ChainLogger)
        ChainLoggerMiddleware._base_logger = logger

        if callable(before_request):
            self._before_request = before_request
            self.before_request = before_request
        else:
            async def before_request_call(request: Request):
                logger = await get_chained_logger(request)
                if self._before_request:
                    logger.info(f"Received {request.method} {request.url.path}")
            self.before_request = before_request_call
            self._before_request = before_request

        if callable(after_request):
            self._after_request = after_request
            self.after_request = after_request
        else:
            async def after_request_call(request: Request, response: Response):
                logger = await get_chained_logger(request)
                if self._after_request:
                    logger.info(f"Request done in {logger.time_elapsed}ms")
            self.after_request = after_request_call
            self._after_request = after_request

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if inspect.iscoroutinefunction(self.before_request):
            await self.before_request(request)
        else:
            self.before_request(request)

        response = await call_next(request)

        if inspect.iscoroutinefunction(self.after_request):
            await self.after_request(request, response)
        else:
            self.after_request(request, response)
        return response

    @staticmethod
    async def initiate_logger(request: Request):
        logger = await ChainLoggerMiddleware._base_logger.get_child_logger()
        root_logger = logging.getLogger()
        root_logger.setLevel(ChainLoggerMiddleware._base_logger._filter.level)
        root_logger.handlers = logger.handlers
        request.state._logger = logger
