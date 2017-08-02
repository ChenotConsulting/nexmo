"""
This file contains all functions required to interact with Nexmo's voice API, including conferencing, TTS, etc...
"""

import urllib
from urllib2 import urlopen, URLError, Request
import sys
import json
import numbers
import config