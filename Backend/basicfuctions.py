import sys
from os import path
from time import strftime, gmtime
from cachetools import cached
import geocoder


@cached(cache={})
def get_package_root():
    """
    This function gets the package root.
    @return: The root of the package.
    """
    # because of python glitch __file__ can't be used when compiled
    # note: __file__ needs to be the base of the project
    return path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)


@cached(cache={})
def get_location():
    g = geocoder.ip('me')
    return g


@cached(cache={})
def get_system_time_offset():
    """gets the system time offset"""
    # TODO fix
    timezone = strftime("%z", gmtime())
    return timezone[:3] + ':' + timezone[3:]


if __name__ == "__main__":
    print(get_location())
