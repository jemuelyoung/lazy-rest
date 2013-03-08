"""
Author: Jem Young - jemuel.young@gmail.com
Date: 3/2013
"""

from sys import argv
from urllib2 import URLError
import urllib
import urllib2

class LazyRest():
           
    def input_processing(self):
        if len(argv) > 1:
            url = argv[1]
        else:
            url = raw_input("URL: ")
        # make sure input is valid url
        if not url.startswith("http://"):
            self.url = "http://" + url
        self.data ={}
        # if data is provided, pass and format to data dict
        if len(argv) > 2:
            data_values = {}
            for index in range(len(argv)):
                if index < 2:
                    continue
                tmp = str(argv[index]).split(':')
                data_values[tmp[0]] = tmp[1]
                
            self.data = urllib.urlencode(data_values)
        
    def execute(self, url):
        request = urllib2.Request(url)
        request.add_header = ('Accept', '*')
           
        try:
            if self.data:
                response = urllib2.urlopen(request, self.data)
            else:
                response = urllib2.urlopen(request)
            print response.read()
        except (URLError):
            print "Could not resolve url"
            
    def run(self):
        self.input_processing()
        self.execute(self.url)
    
lr = LazyRest()    
lr.run()
