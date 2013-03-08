"""
Author: Jem Young - jemuel.young@gmail.com
Date: 3/2013
"""

import urllib
import urllib2
from urllib2 import URLError

class LazyRest():
           
    def input_processing(self):
        url = raw_input("URL: ")
        # make sure input is valid url
        if not url.startswith("http://"):
            self.url = "http://" + url
    
    def execute(self, url):
        request = urllib2.Request(url)
        request.add_header = ('Accept', 'application/json')
        try:
            response = urllib2.urlopen(request)
            response.read()
        except (URLError):
            print "Could not resolve url"
            
    def run(self):
        self.input_processing()
        self.execute(self.url)
    
lr = LazyRest()    
lr.run()
