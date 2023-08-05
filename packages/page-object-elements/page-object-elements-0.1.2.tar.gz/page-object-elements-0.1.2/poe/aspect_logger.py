import os
import sys
import logging
import time
import functools
import inspect
import itertools
import traceback
from datetime import datetime
from pathlib import Path
from selenium.webdriver.remote.webelement import WebElement
from poe.utility import get_all_methods_and_properties

LOG_PATH = Path(os.path.dirname(os.path.realpath(__file__))).parent / "logs" / "test_logs"


class TestLogger(logging.Logger):
    def __init__(self, *, test_name="default"):
        super().__init__("test_logger")
        self.level = logging.DEBUG
        self.addHandler(_StdOutHHandler())
        self.addHandler(TxtFileHandler(test_name=test_name))
        self.handled_element_exceptions: list[dict[
                                              str:str,
                                              str:str,
                                              str:list[str],
                                              str:bool]] = []


class _StdOutHHandler(logging.StreamHandler):
    def __init__(self):
        self.stream = sys.stdout
        self.level = logging.DEBUG
        super().__init__(self.stream)
        self.setFormatter(StdOutFormatter())


class TxtFileHandler(logging.FileHandler):
    def __init__(self, *, test_name):
        self.filename = f"{test_name}_{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"
        LOG_PATH.mkdir(exist_ok=True, parents=True)
        super().__init__(str(LOG_PATH / self.filename))
        self.setFormatter(TxtFileFormatter())


class TxtFileFormatter(logging.Formatter):
    def __init__(self):
        self.fmt = '%(asctime)s | %(levelname)8s | %(message)s'
        super().__init__(self.fmt)


class StdOutFormatter(logging.Formatter):
    """Logging colored formatter for stdout"""
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self):
        super().__init__()
        self.fmt = '%(asctime)s | %(levelname)8s | %(message)s'
        self.formats = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class LoggedProperty(object):
    def __init__(self, name, prop, doc=None):
        self._name = name
        self.fget = prop.fget
        self.fset = prop.fset
        self.fdel = prop.fdel
        if doc is None and prop.fget is not None:
            doc = prop.fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("Unreadable attribute")
        ret_value = self.fget(obj)
        if getattr(obj, 'logger', None):
            obj.logger.debug("Exit {}::{}::{} retrieve. Value: {}".format(
                obj.__module__,
                obj.__class__.__name__,
                self._name, ret_value))
        return ret_value

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("Can't set attribute")
        if getattr(obj, 'logger', None):
            obj.logger.debug("Enter set {}::{}::{} to value: {}".format(
                obj.__module__,
                obj.__class__.__name__,
                self._name, value))
        self.fset(obj, value)
        if getattr(obj, 'logger', None):
            obj.logger.debug("Exit set {}::{}::{} to value: {}".format(
                obj.__module__,
                obj.__class__.__name__,
                self._name, value))

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("Can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel)


# ####################################################### #
# ############### METHOD EXECUTION TIMER ################ #
# ####################################################### #

def timer(func):
    """
    Annotation for measuring time needed for some method to execute
    """

    @functools.wraps(func)
    def function_logger(*args, **kwargs):
        logger.debug(
            f'Enter: {func.__module__}::{args[0].__class__.__name__}::{func.__name__} -> *args: {args} **kwargs: {kwargs}')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        logger.debug(
            'Execution time: {} \t->\t {}::{}::{}()'.format(end - start, func.__module__, args[0].__class__.__name__,
                                                            func.__name__))

    return function_logger


# ####################################################### #
# ################ CLASS LEVEL LOGGING ################## #
# ####################################################### #

def is_locator_none_on_screen_element(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
    except AttributeError as e:
        if e.name in get_all_methods_and_properties(WebElement):
            errmsg = f'{e.args[0]}. To be referenced as a <WebElement> ScreenElement.locator property can`t be None.'
            logger.error('\n'.join([str(errmsg), traceback.format_exc()]))
            raise AttributeError(errmsg)
        raise e
    except Exception as e:
        logger.debug('\n'.join([str(e), traceback.format_exc()]))
        raise e
    return result


def exception_logger(func):
    @functools.wraps(func)
    def function_logger(*args, **kwargs):
        logger.debug('Enter: {}::{}::{} -> *args: {} **kwargs: {}'
                     .format(func.__module__, args[0].__class__.__name__, func.__name__, args, kwargs))
        is_locator_none_on_screen_element(func, *args, **kwargs)
        logger.debug('Exit: {}::{}::{}'.format(func.__module__, args[0].__class__.__name__, func.__name__))

    return function_logger


def log_function(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        logger.debug("Enter {}::{}({}) -> *args: {} **kwargs: {}".format(
            func.__module__, func.__name__, '{}'.format(', '.join(
                ['{}'.format(x) for x in args[1:]] + ['{}={}'.format(k, v) for k, v in iter(kwargs.items())])), args,
            kwargs))
        result = func(*args, **kwargs)
        logger.debug("Exit {}::{}. Result: {}".format(func.__module__, func.__name__, result))
        return result

    return wrapped


def log_method(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if isinstance(logger, TestLogger):
            logger.debug("Enter {}::{}::{}({}) -> *args: {} **kwargs: {}".format(
                args[0].__module__, args[0].__class__.__name__, func.__name__,
                '{}'.format(', '.join(
                    ['{}'.format(x) for x in args[1:]] + ['{}={}'.format(k, v) for k, v in iter(kwargs.items())])),
                args, kwargs))
        result = func(*args, **kwargs)
        if isinstance(logger, TestLogger):
            logger.debug("Exit {}::{}::{}. Result: {}".format(
                args[0].__module__, args[0].__class__.__name__, func.__name__, result))
        return result

    return wrapped


def _log_class_methods_and_properties(cls, skip_list=None):
    mro = inspect.getmro(cls)
    names = [name for name, _ in itertools.chain(*(inspect.getmembers(parent) for parent in mro[1:]))]
    for name, member in inspect.getmembers(cls, lambda m: inspect.ismethod(m) or isinstance(m, property)):
        if name not in names or name == '__init__':
            if skip_list is not None and name in skip_list:
                continue
            if not isinstance(member, property):
                setattr(cls, name, log_method(member))
                continue
            setattr(cls, name, LoggedProperty(name, member))
    return cls


def log(something):
    if inspect.isclass(something):
        skip_list = getattr(something, 'skip_log', [])
        assert isinstance(skip_list, list)
        return _log_class_methods_and_properties(something, skip_list)
    elif inspect.ismethod(something):
        return log_method(something)
    elif inspect.isfunction(something):
        if 'self' in something.__code__.co_varnames:
            return log_method(something)
        return log_function(something)


logger = TestLogger()

if __name__ == '__main__':
    logger.info("test")
    logger.debug("test")
    logger.warning("test")
    logger.error("test")
    logger.fatal("test")
