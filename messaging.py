"""
This file contains all functions required to interact with Nexmo's messaging API, including SMS.
"""

import urllib
from urllib2 import urlopen, URLError, Request
import sys
import json
import numbers
import config.config as config
'''import nexmo'''

action = "sms/"

def sendsms():
    """Sends an SMS to mobile number"""
    recipient = raw_input("Please enter the recipient number to send the sms to, including the country code without 00 or + (e.g. 447456345678): ")
    print(recipient)

    '''print("\nYour available numbers are:" )
    print(numbers.lookupnumbers())'''
    sender = raw_input("Please enter your sender ID. This can be a phone number or some text: ")
    print(sender)

    body = raw_input("Please enter the content of your message: ")
    print(body)

    params = {
        "api_key": config.api_key,
        "api_secret": config.api_secret,
        "from": sender,
        "to": recipient,
        "text": body
    }

    requesturl = config.rest_base_url + action + config.json_response_type
    requestdata = urllib.urlencode(params)
    request = Request(requesturl, data=requestdata)
    '''client = nexmo.Client(key=config.api_key, secret=config.api_secret)'''

    try:
        response = urlopen(request)
        data = response.read()

        '''response = client.send_message({'from': sender, 'to': recipient, 'text': body})
        response = response['messages'][0]'''

        if response.code == 200:
            print(data)
        else:
            print("HTTP response: " + response.code)
    except URLError as e:
        print(e)

def main():
    """This is the default function that runs when the program starts"""
    sendsms()

main()
