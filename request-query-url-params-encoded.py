import urllib
import requests
# google
#
# search?q=test
import urllib.parse

query = []

def searchGoogle(query):

        URL = "https://google.com/search?q={}".format(query)

        encoded_URL = urllib.parse.quote(URL,safe="https://google.com/search?q=")

        print(encoded_URL)
        print(requests.get(encoded_URL).status_code)
        print(requests.get(encoded_URL).text)
searchGoogle("twitter + selling + content")