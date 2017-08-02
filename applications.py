"""
This file contains all functions required to interact with Nexmo's dev API to manage applications required for voice API
"""

import urllib
from urllib2 import urlopen, URLError, Request
import sys
import json
import config