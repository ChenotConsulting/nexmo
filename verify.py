"""
This file contains all functions required to interact with Nexmo's verify API.
"""

import urllib
from urllib2 import urlopen, URLError, Request
import sys
import json
import numbers
import config.config as config
'''import nexmo'''

action = "verify/"

def verifyNumber():
    """Send a PIN code to a mobile number"""
    action = "verify/"

    recipient = raw_input("Please enter the recipient number to send the PIN code to: ")
    print(recipient)

    sender = raw_input("Please enter your sender ID. This can be an alphanumeric string of maximum 11 characters length: ")
    while len(sender) > 11:
        sender = raw_input("You have entered more than 11 characters. Please try again: ")
    print(sender)

    code_length = raw_input("Please select a code length. This can be either 4 or 6 digits. Enter 4 or 6: ")
    print(code_length + " digits")

    pin_expiry = raw_input("Please select the PIN expiry between 60 and 3600 seconds: ")
    print(pin_expiry + " seconds")
    
    next_event_wait = raw_input("Please select the wait time before the next event is triggered between 60 and 900 seconds: ")
    print(next_event_wait + " seconds")

    params = {
        "api_key": config.api_key,
        "api_secret": config.api_secret,
        "brand": "JPC Brand",
        "number": recipient,
        "sender_id": sender,
        "code_length": code_length,
        "lg": "en-US",
        "pin_expiry": pin_expiry,
        "next_event_wait": next_event_wait
    }

    requesturl = config.api_base_url + action + config.json_response_type
    requestdata = urllib.urlencode(params)
    request = Request(requesturl, data=requestdata)

    try:
        response = urlopen(request)
        data = response.read()

        if response.code == 200:
            print(data)
        else:
            print("HTTP response: " + response.code)
    except URLError as e:
        print(e)

def checkVerification():
    """Check that a PIN code is valid"""
    action = "verify/check/"

    requestID = raw_input("Please enter the request ID to cancel: ")
    print(requestID)

    pin_code = raw_input("Please enter the PIN code received: ")
    print (pin_code)

    params = {
        "api_key": config.api_key,
        "api_secret": config.api_secret,
        "request_id": requestID,
        "code": pin_code
    }

    requesturl = config.api_base_url + action + config.json_response_type
    requestdata = urllib.urlencode(params)
    request = Request(requesturl, data=requestdata)

    try:
        response = urlopen(request)
        data = response.read()

        if response.code == 200:
            print(data)
        else:
            print("HTTP response: " + response.code)
    except URLError as e:
        print(e)

def searchRequest():
    """Search all requests"""
    action = "verify/search/"
    
    request_id = raw_input("Please enter the request ID to search for: ")
    print request_id

    params = {
        "api_key": config.api_key,
        "api_secret": config.api_secret,
        "request_id": request_id
    }

    requesturl = config.api_base_url + action + config.json_response_type
    requestdata = urllib.urlencode(params)
    request = Request(requesturl, data=requestdata)

    try:
        response = urlopen(request)
        data = response.read()

        if response.code == 200:
            print(data)
        else:
            print("HTTP response: " + response.code)
    except URLError as e:
        print(e)

def cancelVerificationRequest():
    """Cancel a verification request"""
    action = "verify/control/"

    requestID = raw_input("Please enter the request ID to cancel: ")
    print(requestID)

    params = {
        "api_key": config.api_key,
        "api_secret": config.api_secret,
        "request_id": requestID,
        "cmd": "cancel"
    }

    requesturl = config.api_base_url + action + config.json_response_type
    requestdata = urllib.urlencode(params)
    request = Request(requesturl, data=requestdata)

    try:
        response = urlopen(request)
        data = response.read()

        if response.code == 200:
            print(data)
        else:
            print("HTTP response: " + response.code)
    except URLError as e:
        print(e)

def main():
    """This function is ran by default when the program starts"""

    if len(sys.argv) > 2:
        print("Please enter only one argument!")
    if len(sys.argv) == 1:
        verifyNumber()
    else:
        if sys.argv[1] == "verify":
            verifyNumber()
        if sys.argv[1] == "check":
            checkVerification()
        if sys.argv[1] == "search":
            searchRequest()
        if sys.argv[1] == "cancel":
            cancelVerificationRequest()

main()