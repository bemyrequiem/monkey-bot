import datetime
import platform
import sys

from .cogs import *
from .tools import *
from .config import *
from .events import *
from .messages import *

def version():
    return "v0.0.0.1"

def time():
    return datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

def year():
    return str(datetime.datetime.now().year)

def platform():
    return platform.system() + " " + platform.release()

def path():
    return sys.path