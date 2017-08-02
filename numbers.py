"""
This file allows users to search for available phone numbers in Nexmo's system via an API call.
It also allows to buy phone numbers based on the results of the search.
"""

from urllib2 import Request, urlopen, URLError
import urllib
import json
import sys
import config

#Declare global variables here
base_url = config.rest_base_url
api_key = config.api_key
api_secret = config.api_secret

def startsearch():
    """Gathers input from the user to search numbers from Nexmo"""

    # Prompt to select a country for the number
    country = raw_input("Please enter a country from GB, FR, IE or US: ")
    print(country)
    # Prompt to select a pattern
    #pattern = raw_input("Please enter a phone pattern that you would like to search for (e.g. 1234). You can leave this blank if not required: ")
    #print(pattern)
    #search_pattern = raw_input("Where would you like the pattern to be applied in the number? User 0 to search at the start, use 1 to search anywhere or use 2 to search at the end. You can leave this blank if not required: ")
    #print(search_pattern)
    feature = raw_input("Please enter what type of number you would like to rent. Enter SMS for SMS, VOICE for Voice or SMS,VOICE for both: ")
    print(feature)

    searchnumbers(country, "", "", feature)

"""This function allows the user to buy a number from Nexmo"""
def buynumber(country, msisdn):
    action = "number/buy/"

    params = {
        'api_key': api_key,
        'api_secret': api_secret,
        'country': country,
        'msisdn': msisdn
    }

    requesturl = base_url + action
    requestdata = urllib.urlencode(params)
    print(requesturl)
    request = Request(requesturl, data=requestdata)

    try:
        response = urlopen(request)
        data = response.read()
        
        if response.code == 200:
            print("Virtual number %s rented!" % msisdn)
        else:
            print("HTTP Response: " + response.code)
            print(data)
    except URLError as e:
        print(e)

def searchnumbers(country, pattern, search_pattern, feature):
    """Searches for available numbers from Nexmo"""
    
    action = "number/search?"

    params = {
        'api_key': api_key,
        'api_secret': api_secret,
        'country': country,
        'features': feature,
        'size': 10,
        'index': 1
    }

    requesturl = base_url + action + urllib.urlencode(params)
    #print(requesturl)
    request = Request(requesturl)

    try:
        response = urlopen(request)
        data = response.read()
        numbers = json.loads(data.decode('utf-8'))

        if response.code == 200:
            if len(numbers) > 0:
                for number in numbers['numbers']:
                    print(number)

                msisdn = raw_input("Please enter the number that you would like to purchase (enter none if you don't want to rent a number: ")
                if msisdn.lower() == "none":
                    print("Thank you for using Nexmo. We hope to see you again soon!")
                    quit()
                else:
                    buynumber(country, msisdn)
            else:
                print("There are no numbers available.")
        else:
            print("HTTP response: " + response.code)
    except URLError as e:
        print(e)

def lookupnumbers():
    """This function retrieves the numbers for an account"""

    action = "account/numbers?"

    params = {
        "api_key": api_key,
        "api_secret": api_secret
    }

    requesturl = base_url + action + urllib.urlencode(params)
    #print(requesturl)
    request = Request(requesturl)

    try:
        response = urlopen(request)
        data = response.read()
        numbers = json.loads(data.decode('utf-8'))

        if response.code == 200:
            if len(numbers) > 0:
                for number in numbers['numbers']:
                    print(number['msisdn'])
            else:
                print("There are no numbers associated to your account.")
        else:
            print("HTTP response: " + response.code)
    except URLError as e:
        print(e)

def main():
    """This function is ran by default when the program starts"""

    if len(sys.argv) > 2:
        print("Please enter only one argument!")
    if len(sys.argv) == 1:
        None
    else:
        if sys.argv[1] == "lookup":
            lookupnumbers()
        if sys.argv[1] == "buy":
            startsearch()

main()
