"""
Author: Jem Young - jemuel.young@gmail.com
Date: 3/2013
"""

import urllib
import urllib2

url = raw_input("URL: ").strip()
request = urllib2.Request(url)
request.add_header = ('Accept', 'application/json')
response = urllib2.urlopen(request)
response.read()

